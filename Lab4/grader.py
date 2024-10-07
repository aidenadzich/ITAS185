grade = 1

while grade > 0:
    grade = float(input("Enter your grade: "))

    if grade < 60:
        result = "poor"

    elif grade > 60:
        result = "Passed"

    elif grade == 100:
        result = "Perfect"

    elif grade == 60:
        result = "Squeaked by"

    elif grade < 0:
        result = "Error"

    elif grade > 100:
        result = "Error"
    print(f"Your mark of {grade} means the result was {result}")
    