# exam.py - simple online exam system (console version)

ADMIN_PASSWORD = "admin123"

questions = [
    {"q": "What is 2 + 2?", "options": ["3", "4", "5"], "answer": 2},
    {"q": "Capital of France?", "options": ["Paris", "Rome", "Madrid"], "answer": 1},
    {"q": "Which is a programming language?", "options": ["Python", "Cobra", "HTML"], "answer": 1},
]


def login(username, password):
    if username == "admin" and password == ADMIN_PASSWORD:
        return True
    return False


def run_exam():
    score = 0
    for item in questions:
        print(item["q"])
        for i in range(len(item["options"])):
            print(str(i + 1) + ". " + item["options"][i])
        try:
            choice = int(input("Your answer: "))
        except:
            choice = 0
        if choice == item["answer"]:
            score = score + 1
    return score


def show_result(score):
    total = len(questions)
    percent = score / total * 100
    if percent >= 80:
        print("Grade: A")
    elif percent >= 60:
        print("Grade: B")
    elif percent >= 40:
        print("Grade: C")
    else:
        print("Grade: F")
    print("Score:", score, "/", total)


if __name__ == "__main__":
    final_score = run_exam()
    show_result(final_score)
