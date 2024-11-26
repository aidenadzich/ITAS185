from random import randint

secret_number = randint(1, 100)
user_guess = None

class GreaterThan100Exception(ValueError):
    pass


class LessThan1Exception(ValueError):
    pass


while True:
    try:
        while user_guess != secret_number:

            user_guess = input(f"Enter a number between 1 & 100: ")
            if user_guess == 'q':
                raise KeyboardInterrupt
            user_guess = int(user_guess)

           # assert user_guess < secret_number, "Guess too high!"
           # assert user_guess > secret_number, "Guess too low!"

            if user_guess > secret_number:
                raise GreaterThan100Exception
            if user_guess < secret_number:
                raise LessThan1Exception
            
            
        if user_guess == secret_number:
            print(f"Congrats! The secret number was: {secret_number}")
            user_guess == None
            secret_number = randint(1, 100)
        

    except ValueError:
        print(f"{user_guess} is not an int!")

    except AssertionError as e:
        print(e)

    except GreaterThan100Exception:
        print("Guess too high!")

    except LessThan1Exception:
        print("Guess too low!")

    except KeyboardInterrupt:
        print(f"Thanks for playing!")
        print(f"The secret number was: {secret_number}")
        exit(0)