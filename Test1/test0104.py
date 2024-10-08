"""
AIDEN A - TEST 1 - ITAS185
This program calculates how many times a frog would have to hop to get to the end of a log with a length determined by the user
"""
log_length = float(input("How long is the log? (m): "))
distance_remaining = log_length
number_of_hops = 0

while distance_remaining > 1:
    distance_remaining /= 2
    print(f"The distance remaining is {distance_remaining:.2f}m")
    number_of_hops += 1

print("Going for a swim!")
print(f"It took the frog {number_of_hops} hops to reach the end of the {log_length:.2f}m log.")