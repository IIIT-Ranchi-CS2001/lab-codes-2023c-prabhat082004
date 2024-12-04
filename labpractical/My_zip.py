# Trivia questions stored as a list of dictionaries
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Jane Austen", "C. Mark Twain", "D. Charles Dickens"],
        "answer": "A"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"],
        "answer": "C"
    },
    {
        "question": "Which programming language is named after a comedy group?",
        "options": ["A. Java", "B. Python", "C. Ruby", "D. C++"],
        "answer": "B"
    }
]

# Initialize score
score = 0

# Introduction
print("Welcome to the Trivia Quiz!\n")
print("For each question, type the letter of your answer (A, B, C, or D).\n")

# Quiz loop
for i, q in enumerate(questions, start=1):
    print(f"Question {i}: {q['question']}")
    for option in q['options']:
        print(option)
    user_answer = input("Your answer: ").strip().upper()

    if user_answer == q['answer']:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['answer']}.\n")

# Display final score
print(f"Quiz Over! You scored {score}/{len(questions)}.")

# Feedback based on performance
if score == len(questions):
    print("Excellent! You're a trivia master!")
elif score >= len(questions) // 2:
    print("Good job! You did well!")
else:
    print("Better luck next time!")
