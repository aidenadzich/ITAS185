number = int(input("Enter a number: "))
the_sum = 0
loop_iterator = 1
range_list = [*range(1, number+1)]
print(range_list)

for x in range_list:
    the_sum += loop_iterator
    loop_iterator += 1



print(f"The number you entered was {number} and the sum was {the_sum}")