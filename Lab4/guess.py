import random as ran

my_guess = 0
guesses = 0
play_again = "y"
while play_again == "y":
    guessing_number = ran.randint(1, 100)
    print(f"{guessing_number}")

    while my_guess != guessing_number:
        my_guess = int(input("Enter a number between 1-100: "))
        #guesses += 1
        if guessing_number > my_guess:
            print("Your guess is too low!")
        elif guessing_number < my_guess:
            print("Your guess it too high!")
    if guessing_number == my_guess:
        print(f"Congrats! The number was {guessing_number}, and it took you {guesses} guesses!")
        play_again = input("Play Again? (Y/N): ")


