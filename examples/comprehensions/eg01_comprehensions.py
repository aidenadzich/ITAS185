start = [1, 3, 4, 7, 9, 18]

end = []

for item in start:
    end.append(item * item)
    print(end)

print(f'After loop {end}')

end2 = [_ * _ for _ in start]
print(end2)

end3 = [_ ** 3 for _ in range(3,16)]
print(end3)

every_second = [_ for _ in range(1, 101, 2)]
print(every_second)