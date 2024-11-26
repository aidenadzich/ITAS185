from string import ascii_lowercase

class LongerThan1Exception(ValueError):
    pass

class IsNotLetterException(ValueError):
    pass

letter_count = 0

while True:
    try:
        

        letter = input("Enter a letter: ")

        if len(letter) > 1:
            raise LongerThan1Exception
        
        if letter.isalpha() != True:
            raise IsNotLetterException
        
        file = input("Enter the name of a file: ")

        with open(file, 'r') as file_obj:
            for _ in file_obj:
                for l in _:
                    if l.lower == letter.lower:
                        letter_count += 1
        
        print(letter_count)
        

    except LongerThan1Exception:
        print("Please enter a single letter")
        
    except IsNotLetterException:
        print(f"{letter} is not a letter!")

    except FileNotFoundError:
        print(f"File does not exist!")

    except KeyboardInterrupt:
        print(f"Thank you, goodbye!")
        exit(0)