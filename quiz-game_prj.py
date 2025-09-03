#quiz_game.py

import time

quiz = {
    "What is the capital of France? ": "Paris",
    "Which language is used for web apps? ": "Python",
    "What is 5 + 7? ": "12",
    "Who developed Python? ": "Guido van Rossum"
}

score = 0
time_limit = 10  # seconds per question
username = input("Enter your name: ")

for question, answer in quiz.items():
    print(f"\n⏰ You have {time_limit} seconds to answer!")
    print(question)
    start = time.time()

    user_answer = input("Your answer: ")
    end = time.time()

    if end - start > time_limit:
        print("⏳ Time’s up! No points awarded.")
        continue

    if user_answer.strip().lower() == answer.lower():
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {answer}")

# Show final score
print(f"\n🎯 {username}, your final score is {score}/{len(quiz)}")

# Save to file
with open("scores.txt", "a") as f:
    f.write(f"{username}: {score}/{len(quiz)}\n")

print("📁 Score saved to scores.txt")
