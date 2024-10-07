speed = 0
time = 0
while speed <= 0:
    speed = float(input("Enter your speed: "))

    if speed <= 0:
        print("Invalid speed!")


while time <= 0 or time > 24:
    time = float(input("Enter your time travelling: "))

    if time <= 0:
        print("Invalid Time")
    elif time > 24:
        print("Invalid Time")

increment = 0
print("{:<}".format("Hours | "), "{:>10}".format("Distance (km)"))

while increment < time:
    sum = increment * speed
    print(f"{increment:>5} | {sum:>14.2f}")
    increment += 1
