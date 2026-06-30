import os
import json
from dotenv import load_dotenv
from groq import Groq
from checker import check_safety,check_chat_format
load_dotenv()
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
topics = [
    "career delay in Hindi",
    "love marriage",
    "government job",
    "health anxiety",
    "business advice",
    "foreign travel",
    "study stress",
    "gemstone advice",
    "skeptical user",
    "sade sati"
]
SYSTEM_PROMPT = """
You are Vedaz's AI Vedic astrologer.
Rules:
- Return ONLY valid JSON.
- Do not use markdown.
- Never predict death.
- Never predict disease.
- Never guarantee money.
- Never use fear.
- Remedies are optional spiritual practices, not guarantees.
Output format:
{
"id":"...",
"tags":["..."],
"messages":[
{"role":"system","content":"..."},
{"role":"user","content":"..."},
{"role":"assistant","content":"..."}
]
}
"""
def generate_chat(topic):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.8,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"Generate one conversation about: {topic}"
            }
        ]
    )
    return response.choices[0].message.content
def main():
    output_file = "generated_chats.jsonl"
    saved = 0
    with open(output_file, "w", encoding="utf-8") as f:
        for topic in topics:
            print(f"Generating: {topic}")
            try:
                text = generate_chat(topic)
                start = text.find("{")
                end = text.rfind("}") + 1
                clean_text = text[start:end]    
                chat = json.loads(clean_text)
                issues=check_safety(chat)
                format_ok=check_chat_format(chat)

                if not format_ok:
                    print("Warning: Chat format issue")

                if len(issues)==0:
                    f.write(json.dumps(chat,ensure_ascii=False)+"\n")
                    saved+=1
                    print("Saved")
                else:
                    print("Rejected:",issues)
            except Exception as e:
                print("Error:", e)
    print("\nFinished!")
    print("Total Saved:", saved)
if __name__ == "__main__":
    main()
