# todo: append values to a file
x = []
file_out = open('readwritefile.txt', 'r+')
for i in range(3):
    x.append(file_out.readline().strip('_- \n'))
print(f'{x!r}')

for j in range(5):
    file_out.write(f'This is a line {j}')

file_out.close()