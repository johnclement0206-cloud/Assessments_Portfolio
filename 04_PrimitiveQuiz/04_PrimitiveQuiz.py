# ask the question and get user response
print("What is the capital of France?")
user_answer = input("Your answer: ")

# evaluate answer and provide feedback
correct_answer = "Paris"

if user_answer == correct_answer:
    print("Correct! Paris is the capital of France.")
else:
    print(f"Wrong! The correct answer is {correct_answer}.")
