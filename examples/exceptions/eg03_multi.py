print(f"Enter two numbers or 'q' to exit")

while True:
    x = input("First Number: ")
    if x.lower == 'q':
        break
    y = input("Second Number: ")
    if y.lower == 'q':
        break
    try:
        result = int(x) / int(y)
    except ValueError:
        print("You must enter a number")
    except ZeroDivisionError as e:
        print(f"Error: {str(e).title()}")
    