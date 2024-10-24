"""
    Name: Aiden Adzich
    Course: ITAS 185 - Introduction to Programming
    Assignment 1: Python Dictionaries
    Description: This program creates a dictionary for storing synonyms.
        allows you to add, update, delete, search, or display all entries
"""

from colorama import Fore, Style

choice = 0
synonym_dict = {}


print(Fore.GREEN + r'''
____    __    ____  _______  __        ______   ______   .___  ___.  _______
\   \  /  \  /   / |   ____||  |      /      | /  __  \  |   \/   | |   ____|
 \   \/    \/   /  |  |__   |  |     |  ,----'|  |  |  | |  \  /  | |  |__
  \            /   |   __|  |  |     |  |     |  |  |  | |  |\/|  | |   __|
   \    /\    /    |  |____ |  `----.|  `----.|  `--'  | |  |  |  | |  |____
    \__/  \__/     |_______||_______| \______| \______/  |__|  |__| |_______|''')
print(Style.RESET_ALL)
print(Fore.BLUE)

def menu():

    '''
    This function displays the main menu
    '''

    print(f'''
    {Fore.LIGHTYELLOW_EX}1. {Fore.BLUE}Add a Word
    {Fore.LIGHTYELLOW_EX}2. {Fore.BLUE}Update a Word
    {Fore.LIGHTYELLOW_EX}3. {Fore.BLUE}Delete a Word
    {Fore.LIGHTYELLOW_EX}4. {Fore.BLUE}Search a Word
    {Fore.LIGHTYELLOW_EX}5. {Fore.BLUE}Display Full List
    {Fore.LIGHTYELLOW_EX}6. {Fore.BLUE}Exit Program\n''')


def add_synonym(synonym_dict):

    '''
    This function is for adding new synonyms to the dictionary
    '''

    word = input(f"\n{Fore.BLUE}Enter your word: {Fore.MAGENTA}")
    synonym = input(f"{Fore.BLUE}Enter a synonym: {Fore.MAGENTA}")
    synonym_dict[word] = synonym
    print(f"{Fore.GREEN}Synonym added: '{word}' -> '{synonym}'")
    word = ''
    synonym = ''

def update_synonym(synonym_dict):

    '''
    This function is for updating existing synonyms in the dictionary
    '''

    word = input(f"\n{Fore.BLUE}Enter your word: {Fore.MAGENTA}")
    if word in synonym_dict:
        synonym = input(f"{Fore.BLUE}Enter a updated synonym: {Fore.MAGENTA}")
        synonym_dict[word] = synonym
        print(f"{Fore.GREEN}Synonym updated: '{word}' -> '{synonym}'")
    else:
        print(f"{Fore.RED}{word} not found in dictionary!")
    word = ''
    synonym = ''

def delete_synonym(synonym_dict):

    '''
    This function is for deleting synonyms from the dictionary
    '''

    word = input(f"\n{Fore.BLUE}Enter the word you would like to remove: {Fore.MAGENTA}")
    if word in synonym_dict:
        synonym_dict.pop(word)
        print(f"{Fore.GREEN}{word} has been removed!")
    else:
        print(f"{Fore.RED}{word} not found in dictionary!")
    word = ''

def search_synonym(synonym_dict):

    '''
    This function searches the dictionary for a specific word
    '''

    word = input(f"\n{Fore.BLUE}Enter the word you would like to search for: {Fore.MAGENTA}")
    if word in synonym_dict:
        print(f"{Fore.GREEN}{word}: {synonym_dict[word]}")
    else:
        print(f"{Fore.RED}{word} not found in dictionary!")
    word = ''

def display_synonyms(synonym_dict):

    '''
    This function displays all synonyms in the dictionary
    '''

    for key, value in synonym_dict.items():
        print(f"{Fore.GREEN}{key}: {value}")


while choice != 6:

    if choice == 0:
        menu()
        choice = int(input(f"Enter a number to choose an option: {Fore.MAGENTA}"))

    if choice == 1:
        add_synonym(synonym_dict)
        choice = 0

    elif choice == 2:
        update_synonym(synonym_dict)
        choice = 0

    elif choice == 3:
        delete_synonym(synonym_dict)
        choice = 0

    elif choice == 4:
        search_synonym(synonym_dict)
        choice = 0

    elif choice == 5:
        display_synonyms(synonym_dict)
        choice = 0

    elif choice == 6:
        print(Fore.RED + r'''
  _______   ______     ______    _______  .______   ____    ____  _______
 /  _____| /  __  \   /  __  \  |       \ |   _  \  \   \  /   / |   ____|
|  |  __  |  |  |  | |  |  |  | |  .--.  ||  |_)  |  \   \/   /  |  |__
|  | |_ | |  |  |  | |  |  |  | |  |  |  ||   _  <    \_    _/   |   __|
|  |__| | |  `--'  | |  `--'  | |  '--'  ||  |_)  |     |  |     |  |____
 \______|  \______/   \______/  |_______/ |______/      |__|     |_______|
''')
        print(Style.RESET_ALL)

    else:
        print("Invalid Option!")
        choice = 0
