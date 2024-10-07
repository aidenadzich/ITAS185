var1 = 0

while var1 != 999:
    var1 = int(input("Enter a number (999 to exit): "))

    if var1 < 999:
        square = var1 ** 2
        cube = var1 ** 3
        print(f"The square of {var1} is {square}")
        print(f"The cube of {var1} is {cube}")

print("Thank you!")