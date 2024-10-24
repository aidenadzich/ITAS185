new_list = [f'{i} x {j} is {i * j}' for i in range(1,4) for j in range(1, 6)]
print(new_list)

num_list = [1,2,3,4]
letter_list = ['a', 'b', 'c', 'd', 'e']

combo_list = [str(number) + letter for number in num_list for letter in letter_list]
print(combo_list)

even_combo_list = [str(number) + letter for number in num_list for letter in letter_list if number % 2 == 0]
print(even_combo_list)