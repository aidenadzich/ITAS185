starting_list = [1, 45, -76, 12, 5, 7, 12, 4, 7, 9, 4, 12, -4, 67, -66, 89]

even_sequence = {i for i in starting_list if i % 2 == 0}
print(even_sequence)

comp_dict = {val: val ** 3 for val in range(11)}
print(comp_dict)