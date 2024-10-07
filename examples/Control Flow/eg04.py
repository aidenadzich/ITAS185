'''
Example match statement
'''
lang = input("What's the programming language you want to learn? ")

match lang.lower():
    case 'javascript':
        print("You could be a web dev")
    case 'python':
        print("You could be a data scientist")
        print("or anything you wanted to be actually")
    case 'php':
        print("This is for backend dev")
    case 'go':
        print("Join the great god of Google")
    case 'java':
        print("You're a MC player, aren't you")
    case _:
        print("Your language is useless.")
    