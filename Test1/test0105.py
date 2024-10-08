"""
AIDEN A - TEST 1 - ITAS185
This program creates a list of user provided values, and displays whether they are even or odd
"""

my_list = []
my_value = 1

while my_value > 0:
    my_value = int(input("Enter a whole number (Enter 0 to finish):"))
    my_list.append(my_value)

my_list.remove(0)
print(my_list)

for item in my_list:
    if item % 2 == 0:
        print(f"The number {item} is even")
    else:
        print(f"The number {item} is odd")