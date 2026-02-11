def greet_student(name):
    return f"Hello, {name}!"


def analyze_scores(scores):
    num_subjects = len(scores)
    average_score = sum(scores) / num_subjects
    return num_subjects, average_score


def evaluate_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"


def main():
    name = "Sanidhya"
    scores = [72, 45, 89, 60, 55]

    greeting = greet_student(name)
    subjects, average = analyze_scores(scores)
    result = evaluate_result(average)

    print(greeting)
    print("Number of subjects:", subjects)
    print("Average score:", average)
    print("Result:", result)


main()
