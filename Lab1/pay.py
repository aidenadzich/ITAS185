"""
    Name: Aiden Adzich
    Course: ITAS 185 - Introduction to Programming
    Lab 1: Printing to the screen
    Description: Calculates Wages.
"""


wage = float(input('Enter the wages per hour: '))
hours = float(input('Enter the number of hours worked: '))
gross_pay = wage * hours
after_tax = float(gross_pay) * 0.77
after_bonus = float(after_tax) * 1.13

print(f'Gross Pay: $ {gross_pay}')
print(f'After Tax: $ {after_tax}')
print(f'Total Pay: $ {after_bonus}')
