var1 = int(input("Enter a value less than 10: "))
var2 = 1
my_list = [*range(1,var1+1)]
print(my_list)

if var1 >= 10:
    print("Invalid number!")

else:
    
    for item in my_list:
        square = var2 ** 2
        cube = var2 ** 3
        print(f"The square of {var2} is {square}")
        print(f"The cube of {var2} is {cube}")
        var2 += 1