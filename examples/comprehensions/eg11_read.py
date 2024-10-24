file_read = open('readfile.txt')

read_info = file_read.read()
print(f"read_info is of type {type(read_info)} and has value {read_info!r}")

file_read.close()