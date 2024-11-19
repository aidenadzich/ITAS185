from datetime import datetime
from fractions import Fraction

today = datetime.now()
print(today)

current_time = today.strftime('%H:%M:%S')
print(current_time)

print(today.strftime('%A'))
print(today.strftime('%a'))

print(today.year)

x = Fraction(2.25)
print(x)