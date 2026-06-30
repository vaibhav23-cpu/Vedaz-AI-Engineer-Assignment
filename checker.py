import json
from difflib import SequenceMatcher
FILE_NAME = "new_chats.jsonl"
unsafe_keywords = {
    "Death Prediction": [
        "will die",
        "die early",
        "short life",
        "death"
    ],
    "Medical Claim": [
        "serious disease",
        "you have cancer",
        "you will become sick"
    ],
    "Financial Guarantee": [
        "lottery number",
        "guaranteed money",
        "become rich",
        "guaranteed profit"
    ],
    "Fear Based Remedy": [
        "life will be ruined",
        "must do this puja",
        "pay",
        "otherwise everything will be ruined"
    ]
}
def load_chats(file_name):
    chats = []
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                chats.append(json.loads(line))
    return chats

def check_chat_format(chat):
    messages = chat.get("messages", [])
    if len(messages) == 0:
        return False
    if messages[0]["role"] != "system":
        return False
    expected_role = "user"
    for msg in messages[1:]:
        if msg["role"] != expected_role:
            return False
        if expected_role == "user":
            expected_role = "assistant"
        else:
            expected_role = "user"
    return True

def count_total_words(chat):
    total_words = 0
    for msg in chat["messages"]:
        total_words += len(msg["content"].split())
    return total_words

def check_duplicates(chats):
    duplicate_list = []
    for i in range(len(chats)):
        first_chat = " ".join(
            message["content"]
            for message in chats[i]["messages"]
        )
        for j in range(i + 1, len(chats)):
            second_chat = " ".join(
                message["content"]
                for message in chats[j]["messages"]
            )
            similarity = SequenceMatcher(
                None,
                first_chat,
                second_chat
            ).ratio()
            if similarity > 0.90:
                duplicate_list.append(
                    (
                        chats[i]["id"],
                        chats[j]["id"]
                    )
                )
    return duplicate_list

def check_safety(chat):
    assistant_text = ""
    for message in chat["messages"]:
        if message["role"] == "assistant":
            assistant_text += message["content"].lower() + " "
    issues = []
    if "you will die" in assistant_text:
        issues.append("Death Prediction")
    if "you have cancer" in assistant_text or "you will become sick" in assistant_text:
        issues.append("Medical Claim")
    if "guaranteed money" in assistant_text or "guaranteed profit" in assistant_text:
        issues.append("Financial Guarantee")
    if "must do this puja" in assistant_text or "life will be ruined" in assistant_text:
        issues.append("Fear Based Remedy")
    return issues

def split_data(chats):
    split_index = int(len(chats) * 0.8)
    train_data = chats[:split_index]
    test_data = chats[split_index:]
    with open("train.jsonl", "w", encoding="utf-8") as train_file:
        for chat in train_data:
            train_file.write(json.dumps(chat, ensure_ascii=False) + "\n")
    with open("test.jsonl", "w", encoding="utf-8") as test_file:
        for chat in test_data:
            test_file.write(json.dumps(chat, ensure_ascii=False) + "\n")
    return len(train_data), len(test_data)

def main():
    print("=" * 50)
    print("VEDAZ CHAT CHECKER")
    print("=" * 50)
    chats = load_chats(FILE_NAME)
    print(f"\nTotal Chats Found : {len(chats)}")
    print("\nChecking Chat Format...\n")
    for chat in chats:
        if check_chat_format(chat):
            print(f"{chat['id']} --> PASS")
        else:
            print(f"{chat['id']} --> FAIL")
    print("\nCounting Words...\n")
    for chat in chats:
        words = count_total_words(chat)
        print(f"{chat['id']} --> {words} words")
    print("\nChecking Duplicate Chats...\n")
    duplicates = check_duplicates(chats)
    if len(duplicates) == 0:
        print("No duplicate chats found.")
    else:
        for item in duplicates:
            print("Duplicate:", item)
    print("\nRunning Safety Checks...\n")
    unsafe_found = False
    for chat in chats:
        result = check_safety(chat)
        if result:
            unsafe_found = True
            print(f"{chat['id']} --> Unsafe")
            print("Reason:", ", ".join(result))
            print()
    if not unsafe_found:
        print("No unsafe conversations found.")
    print("\nCreating Train/Test Split...\n")
    train_size, test_size = split_data(chats)
    print(f"Training Chats : {train_size}")
    print(f"Testing Chats  : {test_size}")
    print("\nFinished Successfully!")
if __name__ == "__main__":
    main()