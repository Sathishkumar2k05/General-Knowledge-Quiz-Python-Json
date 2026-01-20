import json

with open("details.json", "r") as s:

    data = json.load(s)

def quiz():

    score = 0

    print("Welcome to the General Knowledge Quiz\n")

    for q in data:

        print(q["question"])

        for option in q["options"]:

            print(option)

        user_answer = input("Enter your answer (A/B/C/D) : ").upper()

        if user_answer == q["answer"]:

            print("Correct!\n")

            score += 1

        else:

            print(f"Wrong! Correct answer is {q["answer"]}\n")

    print("Quiz Finished!")

    print(f"Your Score : {score}/{len(data)}")

quiz()