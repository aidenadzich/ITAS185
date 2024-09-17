"""
Aiden Adzich
ITAS Lab #2, Parts #A-C
This program demonstrates how numeric types and operators behave in Python

"""
# Add the import statements you need here
import math as m
import random as r
# TASK A- Correct these forumulae
# Find an arithmetic average
# identifier declarations
NUMBER = 3		# number of scores
SCORE1 = 100	# first test score
SCORE2 = 97 	# second test score
SCORE3 = 90     # third test score

average = float((SCORE1 + SCORE2 + SCORE3) / NUMBER)
print(f"{SCORE1} and {SCORE2} and {SCORE3} have an average of {average:.3f}")

# Convert Fahrenheit temperatures to Celsius
BOILING_IN_F = 212      # boiling temperature

f_to_c = (BOILING_IN_F -32) * 5/9

print(f"{BOILING_IN_F} in Fahrenheit is {f_to_c} in Celsius.", end="\n\n")

# ADD LINES FOR TASK B HERE
# Note you also need to import the random module where indicated above
# Next:
#    prompt the user to enter their name and read it in to a variable called first_name
#    prompt the user to enter the lowest number that their lucky number could be and call the variable low
#    prompt the user to enter the highest number that their lucky number could be and call the variable high
#    generate a random integer between low and high and call it lucky_number using the randint function
#    print out a message to the user including their name and lucky number 
first_name = str(input("Enter your name here: "))
low = float(input("Enter the lowest number your lucky number could be: "))
high = float(input("Enter the highest number your lucky number could be: "))
low = int(low)
high = int(high)
lucky_number = r.randint(low, high)

print(f"Hello {first_name}! Your lucky number is: {lucky_number}")


# ADD LINES FOR TASK C HERE
# prompt the user for a diameter of a sphere
# read the diameter
# calculate the radius
# calculate the volume 
# print out the volume

diameter = float(input("Enter the diameter of your circle: "))
radius = diameter / 2
volume = (4/3) * m.pi * radius ** 3
print(f"The volume of the sphere with a diameter of {diameter} is: {volume}")

