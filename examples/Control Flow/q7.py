close = 1
distance = int(input("Enter a number: "))

while close < distance:
    print(f"The worm is {distance} units away")
    distance /= 2

print(f"The worm is {distance} units away. Close enough!")