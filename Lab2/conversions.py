"""
AIDEN A - NUMBER CONVERSIONS
This program lets you select a conveter (or lucky number generator!)
"""

import math as m
import random as r

print(f"""Choose a selection: 
      1. Averages (3 Inputs) 
      2. Fahrenheit -> Celcius Conversion 
      3. Celcius -> Fahrenheit Conversion 
      4. Lucky Number
      5. Volume of a Sphere
      6. Mileage """)
page = float(input())

if page == 1:
    number = int(3)		
    score1 = int(input("Enter the first number: "))	
    score2 = int(input("Enter the second number: ")) 	
    score3 = int(input("Enter the third number: "))    

    average = float((score1 + score2 + score3) / number)
    print(f"{score1} and {score2} and {score3} have an average of {average:.3f}")
    raise SystemExit(0)

if page == 2:
    fahrenheit = float(input("Enter a Fahrenheit value: "))     

    f_to_c = (fahrenheit - 32) * 5/9

    print(f"{fahrenheit} in Fahrenheit is {f_to_c} in Celsius.", end="\n\n")
    raise SystemExit(0)

if page == 3:
    celcius = float(input("Enter a Celcius value: "))     

    c_to_f = (9/5) * celcius + 32

    print(f"{celcius} in Celcius is {c_to_f} in Fahrenheit.", end="\n\n")
    raise SystemExit(0)

if page == 4:
    first_name = str(input("Enter your name here: "))
    low = float(input("Enter the lowest number your lucky number could be: "))
    high = float(input("Enter the highest number your lucky number could be: "))
    low = int(low)
    high = int(high)
    lucky_number = r.randint(low, high)

    print(f"Hello {first_name}! Your lucky number is: {lucky_number}")
    raise SystemExit(0)

if page == 5:
    diameter = float(input("Enter the diameter of your sphere: "))
    radius = diameter / 2
    volume = (4/3) * m.pi * radius ** 3
    print(f"The volume of the sphere with a diameter of {diameter} is: {volume}")

if page == 6:
    kmdriven = float(input("Enter kilometers driven: "))
    litresused = float(input("Enter litres of fuel used: "))
    lpkm = (litresused * 100) / kmdriven
    print(f"If {kmdriven} kilometres are driven using {litresused} litres of fuel, then the vehicle uses {lpkm:.2f} litres for ever 100 kilometers")

else:
    print("Invalid Option!")