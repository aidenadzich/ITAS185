# todo: append again but without reading first
file_out = open('readwritefile.txt', 'a')


for j in range(5):
    file_out.write(f'This is a line {j}')

file_out.close()