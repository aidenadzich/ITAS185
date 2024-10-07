number = int(input("Enter a number: "))
the_sum = 0
loop_iterator = 1
range_list = [*range(1, number+1)]
#print(range_list)

for x in range_list:
    the_sum += loop_iterator
    loop_iterator += 1
print(f"(For) The number you entered was {number} and the sum was {the_sum}")

the_sum = 0
loop_iterator = 1
while number+1 > loop_iterator:
    the_sum += loop_iterator
    loop_iterator += 1


print(f"(While) The number you entered was {number} and the sum was {the_sum}")