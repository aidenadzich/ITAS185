"""
    Name: Aiden Adzich
    Course: ITAS 185 - Introduction to Programming
    Lab 1: Printing to the screen
    Description: Doing various calculations.
"""

num1 = float(input('Enter a number: '))
num2 = float(input('Enter a second number: '))
dif = num2 - num1
prod = num1 * num2
quot = num1 / num2
remain = num1 % num2
integ = num1 // num2

print(f'The difference of {num1} and {num2} is {dif}')
print(f'The product of {num1} and {num2} is {prod}')
print(f'The quotient of {num1} and {num2} is {quot}')
print(f'The remainder of {num1} and {num2} is {remain}')
print(f'The integer division of {num1} and {num2} is {integ}')
