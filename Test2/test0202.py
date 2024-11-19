'''
AIDEN A - TEST 2 Q2 - ITAS185
'''

'''
Opens the text file and reads each lines
'''
with open('input.txt', 'r') as input_file:
    words = input_file.read().splitlines()

print(words)

'''
Finds every word in the file that starts with C
'''
c_list = [_ for _ in words if _.startswith('C') == True]
print(c_list)

'''
Finds every word in the file that ends with h
'''
h_list = [_ for _ in words if _.endswith('h') == True]
print(h_list)

input_file.close()

'''
Writes the list of words that start with C to the file
'''
with open('output.txt', 'w') as output_file:
    for _ in c_list:
        output_file.write(f'{_}\n')
output_file.close()

'''
Appends the list of words that end with h to the file
'''
with open('output.txt', 'a') as output_file:
    for _ in h_list:
        output_file.write(f'{_}\n')
output_file.close()