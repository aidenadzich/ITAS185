set1 = {1, 2, 3}
set2 = {2, 3, 1}
set3 = {3, 2, 1}
set4 = {1, 2, 3, 3, 2, 3, 2, 3, 1, 2, 3, 3, 1, 2, "add", "badger", 4.3, "another string", "abc", "add"}
set5 = {10, 11, 12}
set6 = {3, 4, 5}

print(set1 == set2)
print(set2)
print(set4)

new_set = set1.union(set5)
print(new_set)

new_set2 = set1.intersection(set5)
print(new_set2)