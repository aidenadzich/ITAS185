file_name = 'animals.txt'

try:
    with open(file_name) as file_obj:
        lines = file_obj.readlines()
    
except FileNotFoundError:
    print('The file is not found')

else:
    print('File has been read')

finally:
    print('Finally done')



print("All done")