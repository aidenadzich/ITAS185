var1 = int(input("Enter a value less than 10: "))
var2 = 1

if var1 >= 10:
    print("Invalid number!")

else:
    
    while var2 < var1:
        square = var2 ** 2
        cube = var2 ** 3
        print(f"The square of {var2} is {square}")
        print(f"The cube of {var2} is {cube}")
        var2 += 1