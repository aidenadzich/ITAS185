var1 = int(input("Enter the first number: "))
var2 = int(input("Enter the second number: "))


if var1 > var2:
    print(f"The first number is {var1}")
    print(f"The second number is {var2}")
    print(f"{var1} is greater than {var2}")

elif var1 < var2:
    print(f"The first number is {var1}")
    print(f"The second number is {var2}")
    print(f"{var2} is greater than {var1}")

else:
    print(f"The first number is {var1}")
    print(f"The second number is {var2}")
    print("The numbers are equal")