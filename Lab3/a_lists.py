list_one = [
    -245, 230, -198, 187, -176, 165, -154, 143, -132, 121,
    -110, 99, 88, 77, -66, 55, -44, 33, -22, 11,
    -1, 2, -3, 4, -5, 6, 7, 8, -9, 10,
    -11, 12, -63, 44, -25
]

the_string = f'Everyone knows in a choice between Star Wars and Star Trek the only correct answer is Docter Who'

mixed_list = ["hippo", 2034, 22.34, "old", True, 1, 3, -7.4]

item_two = list_one[1]
print(item_two)

part_b = list_one[5:10]
print(part_b)

print(list_one[0])

print(list_one[-1])

print(list_one[-6:-2])

list_two = [1000, 1234, -234, 45]

end_list = list_one + list_two
print(end_list)

print(55 in list_one)
print(14 in list_one)
print(len(end_list))

list_one[14] = 100
print(list_one)

print(the_string[-10:])
print(the_string[35:45])
print(the_string[:8])
print(the_string[-10:].upper())
print(the_string[35:45].lower())

mixed_list.append('hockey')
print(mixed_list)
mixed_list.insert(2, False)
print(mixed_list)
mixed_list.remove('old')
print(mixed_list)

pop_value = mixed_list.pop(6)
print(pop_value)
print(mixed_list)

new_list = mixed_list.copy()
new_list.append('new')
print(mixed_list)
print(new_list)

range_list = [*range(-10, 12, 2)]
print(range_list)