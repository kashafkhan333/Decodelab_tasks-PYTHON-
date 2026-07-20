# General Knowledge Quiz

print("===================================")
print("     GENERAL KNOWLEDGE QUIZ")
print("===================================\n")

score = 0

# Question 1
answer = input("1. What is the capital of France? ").strip().lower()

if answer == "paris":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Paris.\n")

# Question 2
answer = input("2. Which planet is known as the Red Planet? ").strip().lower()

if answer == "mars":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Mars.\n")

# Question 3
answer = input("3. How many continents are there on Earth? ").strip()

if answer == "7":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is 7.\n")

# Final Score
print("===================================")
print("Quiz Finished!")
print("Your Final Score:", score, "/ 3")

if score == 3:
    print("Excellent! You got all answers correct.")
elif score == 2:
    print("Good job! You scored 2 out of 3.")
elif score == 1:
    print("You scored 1 out of 3. Keep practicing!")
else:
    print("Better luck next time!")
print("===================================")
