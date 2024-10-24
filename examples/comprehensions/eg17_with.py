# todo: using a 'with' loop
with open('readfile.txt') as file_read:
    read_info = file_read.read()

print(f'{read_info}')
print(f'{read_info!r}')

with open('readfile.txt') as file_handle:
    lines = [line.strip() for line in file_handle]

print(f'{lines!r}')