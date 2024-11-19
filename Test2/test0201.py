'''
AIDEN A - TEST 2 Q1 - ITAS185
'''

'''
Checks which numbers between 1 and max_num are divisible by 3, and then cubes them
'''
def cubed(max_num):
    result = [_ ** 3 for _ in range(1, max_num+1) if _ % 3 == 0]
    print(result)


'''
Creates a dict containing every number between lower_num and upper_num
'''
def num_str(lower_num, upper_num):
    num_dict = {_: _ for _ in range(lower_num, upper_num+1)}
    print(num_dict)


'''
Finds all the values in list_a that are NOT in list_b
'''
def common_num(list_a, list_b):
    list_a_values = [_ for _ in list_a if _ not in list_b]
    print(list_a_values)


'''
Finds all the words in the_string that are under 5 letters long
'''
def short_words(the_string):
    words_split = the_string.split()
    words_under_five = [_ for _ in words_split if len(_) < 5]
    print(words_under_five)

    
'''
Check whether the program is running as the main program, if so then test the above functions
'''
if __name__ == "__main__":

    print("Numbers between 1 & max_numer divisible by 3, then cubed")
    cubed(6)
    cubed(16)
    cubed(26)

    print('Numbers between lower_num and upper_num')
    num_str(2, 5)
    num_str(5, 10)
    num_str(10, 20)

    print('Numbers in list_a and not list_b')
    common_num([1, 2, 3, 4], [3, 4, 5, 6])
    common_num([1, 2, 5, 6], [1, 2, 3, 5])
    common_num([7, 8, 9, 1], [1, 5, 4, 3])

    short_words('Find all of the words in a string that are less than 5 letters')
    short_words('He owes me a whole lot of money')
    short_words('Can you please help me?')




