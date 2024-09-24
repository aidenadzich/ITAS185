num_list = [3, 4, 6, 7, 1, 5]
string_list = ["yoda", "obi-wan kenobi", "anakin skywalker", "luke skywalker", "qui-gon jinn", "mace windu"]
mixed_list = ["turkey", 3.14, True, "hamster", 9001]

print(string_list)
print(num_list[2])
string_list.append("yaddle")
print(string_list)

string_list.extend(['ki-adi-mundi', 'yarel poof'])
print(string_list)

string_list.insert(2, 'ahsoka tano')
print(string_list)

string_list.remove('anakin skywalker')
print(string_list)

a2 = [1, 2, 3]
b2 = a2
print(f'a2 is {a2} and b2 is {b2}')

b2.append(5)
print(f'a2 is {a2} and b2 is {b2}')
