def checkAge(the_age):
    if the_age <= 0:
        raise ValueError("Only positive integers allowed")

    if the_age % 2 == 0:
        print("Age is even")
    else:
        print("Age is odd")


try:
    num = int(input("Enter your age: "))
    checkAge(num)

except ValueError as e:
    print(e)

