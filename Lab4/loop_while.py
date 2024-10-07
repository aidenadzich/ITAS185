number = int(input("Enter a number: "))
the_sum = 0
loop_iterator = 1

while number+1 > loop_iterator:
    the_sum += loop_iterator
    loop_iterator += 1

print(f"The number you entered was {number} and the sum was {the_sum}")