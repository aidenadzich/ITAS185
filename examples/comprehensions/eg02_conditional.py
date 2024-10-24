starting_list = [1, 45, -76, 23, 5, 12, 4, 7, 9, 12, 12, -4, -67, -66, 89, -101]

even_list = [item for item in starting_list if item % 2 == 0]
print(even_list)

three_times = [3 * item for item in starting_list if item < 0]
print(three_times)

new_list = [_ for _ in range(101) if _ % 3 == 0 and _ % 7 == 0]
print(new_list)

odd_list = [_ for _ in starting_list if _ % 2 == 1 and _ > 0]
print(odd_list)

even_odd_list = ['even' if item % 2 == 0 else 'odd' for item in range(100)]
print(even_odd_list)

fizz_buzz = ['fizzbuzz' if item % 15 == 0 else 'fizz' if item % 3 == 0 else 'buzz' if item % 5 == 0 else item for item in range(101)]
print(fizz_buzz)