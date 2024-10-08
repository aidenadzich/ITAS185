"""
AIDEN A - TEST 1 - ITAS185
This program tells you your total at a restaurant, and how much each person should pay
"""
restaurant_bill = float(input("Enter the amount of your bill: "))
people = int(input("Enter the number of people for your bill: "))
restaurant_total = restaurant_bill * 1.2
cost_per_person = restaurant_total/people

print(f"The cost of the meal was ${restaurant_bill:.2f}. With tip that makes ${restaurant_total:.2f}. For {people} people the cost per person was ${cost_per_person:.2f} each.")