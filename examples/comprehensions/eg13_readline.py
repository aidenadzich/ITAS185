# todo: read the file readfile.txt one line at a time

file_read = open('readfile.txt')

read_info = file_read.readline()
print(f"read_info is of type {type(read_info)} and contents are {read_info!r}")
read_info = file_read.readline()
print(f'contents are {read_info!r}')


file_read.close()