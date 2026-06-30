<<<<<<< HEAD
# Vedaz AI Engineer Internship Assessment
**Candidate:** Vaibhav Sharma
## Project Overview
This project is my submission for the Vedaz AI Engineer Internship assessment.
The objective of this assignment was to build simple tools for checking, generating, and evaluating AI astrology conversations while following Vedaz's safety guidelines.
The project contains three Python scripts:
- `checker.py`
- `generator.py`
- `quality_tester.py`
---
# Task 1 – Chat Checker
The `checker.py` script validates astrology conversations stored in JSONL format.
It performs the following checks:
- Verifies that every conversation follows the correct message structure.
- Counts the total number of words in each conversation.
- Detects duplicate or very similar conversations.
- Splits the dataset into training and testing files.
- Checks conversations for safety issues such as:
  - Death predictions
  - Medical claims
  - Financial guarantees
  - Fear-based remedies
The safety checks are implemented using keyword matching because it is simple, easy to understand, and works well for this assignment.
---

# Task 2 – Chat Generator
The `generator.py` script automatically creates new astrology conversations using the Groq API and the Llama 3.3 70B model.
The script:
- Generates conversations for different topics.
- Converts the AI response into JSON.
- Runs every generated conversation through the safety checker.
- Saves only valid conversations into `generated_chats.jsonl`.
This helps create additional training data while filtering out unsafe responses.
---

# Task 3 – Quality Tester
The `quality_tester.py` script evaluates the quality of AI responses.
It asks the AI a set of astrology-related questions and then scores each response based on:
- Safety
- Helpfulness
- Honesty
- Overall quality
The final scores are displayed in a simple table.
---

# Technologies Used
- Python 3.11
- Groq API
- Llama 3.3 70B Versatile
- python-dotenv
---

# Installation
Install the required packages:
```bash
pip install groq python-dotenv
```
Create a `.env` file in the project folder and add your API key:

```
# Running the Project
Run the Chat Checker:
```bash
python checker.py
```
Run the Chat Generator:
```bash
python generator.py
```
Run the Quality Tester:
```bash
python quality_tester.py
```
---

# Project Structure
```
Vedaz_Assignment/

 checker.py
 generator.py
 quality_tester.py
 generated_chats.jsonl
 new_chats.jsonl
 train.jsonl
 test.jsonl
 README.md
 .gitignore
 .env
```
---

# Design Decisions
While working on this assignment, I focused on keeping the solution simple and easy to understand.
For safety detection, I used keyword-based checks because they are lightweight and quick to implement. Although this approach may not detect every unsafe response, it provides a good starting point.
For chat generation and evaluation, I used the Groq API with the Llama 3.3 70B model to generate conversations and evaluate response quality.
---

# Future Improvements
If I had more time, I would improve this project by:
- Using semantic similarity instead of simple duplicate matching.
- Replacing keyword safety checks with an LLM-based safety evaluator.
- Generating a larger and more diverse dataset.
- Adding unit tests for each script.
- Creating a simple web interface to run all three tasks.
---

Thank you for reviewing my submission.
=======
# Vedaz-AI-Engineer-Assignment