class NegativeAgeException(RuntimeError):
    pass

class AgeTooLargeException(RuntimeError):
    pass

def checkAge(the_age):
    if the_age <= 0:
        raise NegativeAgeException("Only positive integers allowed")
    
    if the_age >= 120:
        raise AgeTooLargeException("Age too large")

    if the_age % 2 == 0:
        print("Age is even")
    else:
        print("Age is odd")

while True:

    try:
        num = int(input("Enter your age: "))
        checkAge(num)

    except NegativeAgeException as e:
        print(e)

    except AgeTooLargeException as e:
        print(e)

