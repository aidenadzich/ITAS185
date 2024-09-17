"""
Aiden Adzich
ITAS Lab #2, Part #D
This program calculatres litres/100km based on litres and km driven
"""
kilometres_driven = float(input("Enter kilometers driven: "))
litres_used = float(input("Enter litres of fuel used: "))
litres_per_hundred_kilometres = (litres_used * 100) / kilometres_driven
print(f"If {kilometres_driven} kilometres are driven using {litres_used} litres of fuel, then the vehicle uses {litres_per_hundred_kilometres:.2f} litres for ever 100 kilometers")