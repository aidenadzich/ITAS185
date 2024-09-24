"""
ITAS 185
AIDEN ADZICH
LAB 03, PART B
This program shows a range of numbers based on user input using Argv
"""

import sys



print(sys.argv[0][-8:])

num = int(sys.argv[1])

command_list = list(range(1, num + 1))

print(command_list)