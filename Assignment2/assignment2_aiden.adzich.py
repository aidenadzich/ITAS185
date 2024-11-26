"""
    Name: Aiden Adzich
    Course: ITAS 185 - Introduction to Programming
    Assignment 2: Codewords
"""

import random
import string
import pywriter
import colorama as c

class CodeWordsGame:
    """
    A class representing a CodeWords game where a secret word is encoded, and 
    the player has to decode it using hints or guesses.

    Attributes:
        secret_word (str): The randomly selected word to be guessed.
        coded_word (str): The encoded version of the secret word.
        max_hints (int): The maximum number of hints a player can use.
        _hints_used (int): The number of hints already used.
        max_guesses (int): The maximum number of incorrect guesses allowed.
        guesses_used (int): The number of incorrect guesses already made.
        encoding_map (dict): The encoding translation map for letters.
        decoding_map (dict): The decoding translation map for letters.
    """
    
    def __init__(self):
        """
        Initializes the CodeWordsGame with a randomly selected secret word, encodes it, 
        and sets game parameters for hints and guesses.
        """
        self.secret_word = self.select_word().upper()
        self.coded_word = self.encode_word(self.secret_word)
        self.max_hints = 3
        self._hints_used = 0
        self.max_guesses = 3
        self.guesses_used = 0

    def read_file(self):
        """
        Reads a list of potential secret words from a file called 'codewords.txt'.

        Returns:
            list: A list of words read from the file.
        """
        with open('codewords.txt', 'r') as file:
            return [line.strip() for line in file.readlines()]

    def select_word(self):
        """
        Randomly selects a secret word from the list of words.

        Returns:
            str: A randomly chosen word from the list.
        """
        words = self.read_file()
        return random.choice(words)

    def encode_word(self, word):
        """
        Encodes the secret word by randomly shuffling the alphabet.

        Args:
            word (str): The secret word to be encoded.

        Returns:
            str: The encoded version of the secret word.
        """
        shuffled_alpha = ''.join(random.sample(string.ascii_uppercase, len(string.ascii_uppercase)))
        self.encoding_map = str.maketrans(string.ascii_uppercase, shuffled_alpha)
        self.decoding_map = str.maketrans(shuffled_alpha, string.ascii_uppercase)
        return word.translate(self.encoding_map)

    def change_letter(self, letter, substitute):
        """
        Replaces a letter in the coded word with another letter provided by the player.

        Args:
            letter (str): The letter in the coded word to be replaced.
            substitute (str): The letter to replace the original letter.

        Returns:
            bool: True if the coded word matches the secret word after the change; False otherwise.
        """
        letter = letter.upper()
        substitute = substitute.upper()

        if substitute in self.coded_word:
            pywriter.write(f"{c.Fore.RED}The letter {c.Fore.YELLOW}{substitute}{c.Fore.RED} has already been used in the coded word. Choose a different substitute.{c.Style.RESET_ALL}", rate=word_speed)
            return False
        
        if len(letter) > 1:
            pywriter.write(f"{c.Fore.RED}You can only select one letter!{c.Style.RESET_ALL}", rate=word_speed)
            return False

        if letter.isalpha() and substitute.isalpha() and len(substitute) == 1:
            if letter in self.coded_word:
                self.coded_word = self.coded_word.replace(letter, substitute)
                return self.coded_word == self.secret_word
            else:
                pywriter.write(f"{c.Fore.RED}The letter {c.Fore.YELLOW}{letter}{c.Fore.RED} is not part of the original secret word.{c.Style.RESET_ALL}", rate=word_speed)
                return False
        else:
            pywriter.write(f"{c.Fore.RED}Invalid input. Ensure you enter one valid letter for both fields.{c.Style.RESET_ALL}", rate=word_speed)
            return False

    def get_hint(self):
        """
        Provides a hint by decoding one random letter in the coded word.

        Returns:
            tuple: The randomly selected letter and its decoded version, or None if no hints remain.
        """
        if self._hints_used < self.max_hints:
            random_letter = random.choice([_ for _ in self.coded_word if _.isalpha()])
            decoded_letter = random_letter.translate(self.decoding_map)
            self.coded_word = self.coded_word.replace(random_letter, decoded_letter)
            self._hints_used += 1
            return random_letter, decoded_letter
        else:
            return None

    def is_won(self):
        """
        Checks if the player has won the game.

        Returns:
            bool: True if the coded word matches the secret word; False otherwise.
        """
        return self.coded_word == self.secret_word

    def is_lost(self):
        """
        Checks if the player has lost the game by using all guesses.

        Returns:
            bool: True if the number of guesses used is equal to or greater than the max guesses; False otherwise.
        """
        return self.guesses_used >= self.max_guesses

    def __str__(self):
        """
        Provides a string representation of the current game state.

        Returns:
            str: The coded word with color formatting.
        """
        return f'Coded Word: {c.Fore.MAGENTA}{self.coded_word}{c.Style.RESET_ALL}'

    def __repr__(self):
        """
        Provides a detailed representation of the game state for debugging.

        Returns:
            str: A string with all the game attributes.
        """
        return f'CodeWordsGame(secret_word={self.secret_word}, coded_word={self.coded_word}, max_hints={self.max_hints}, hints_used={self._hints_used}, max_guesses={self.max_guesses}, guesses_used={self.guesses_used})'



if __name__ == "__main__":
    game = CodeWordsGame()
    word_speed = 0.03

    pywriter.write(f"""{c.Fore.CYAN}
*------------------------------------------------------*
|   _____          _                            _      |
|  / ____|        | |                          | |     |
| | |     ___   __| | _____      _____  _ __ __| |___  |
| | |    / _ \ / _` |/ _ \ \ /\ / / _ \| '__/ _` / __| |
| | |___| (_) | (_| |  __/\ V  V / (_) | | | (_| \__ \ |
|  \_____\___/ \__,_|\___| \_/\_/ \___/|_|  \__,_|___/ |
|                  By: Aiden Adzich                    |
*------------------------------------------------------*                                  
     """, rate=0.01)

    pywriter.write(f"\nWelcome to CodeWords. I have encoded a phrase as:{c.Fore.MAGENTA} {game.coded_word}", rate = word_speed)
    pywriter.write(f"{c.Fore.GREEN}\nEnter a letter to select it for replacement", rate = word_speed)
    pywriter.write(f"{c.Fore.BLUE}\nEnter {c.Fore.YELLOW}?{c.Fore.BLUE} to use a hint. You have {c.Fore.YELLOW}{game.max_hints}{c.Fore.BLUE} hints available to you", rate = word_speed)
    pywriter.write(f"{c.Fore.BLUE}\nEnter {c.Fore.YELLOW}!{c.Fore.BLUE} to make a guess. You have {c.Fore.YELLOW}{game.max_guesses}{c.Fore.BLUE} guesses. If you run out, game over!", rate = word_speed)
    pywriter.write(f"{c.Fore.RED}\nEnter {c.Fore.YELLOW}.{c.Fore.RED} to exit the program", rate = word_speed)
    print(c.Style.RESET_ALL)
    pywriter.write(f"\n{game}")

    while not game.is_won() and not game.is_lost():
        letter = input("\nMake your selection: ").strip()
        if letter == "?":
            hint = game.get_hint()
            if hint:
                pywriter.write(f"\n{c.Fore.YELLOW}{hint[0]}{c.Style.RESET_ALL} has been replaced with {c.Fore.YELLOW}{hint[1]}{c.Style.RESET_ALL}. Now your phrase is:\n", rate = word_speed)
                pywriter.write(f"{c.Fore.MAGENTA} {game.coded_word} {c.Style.RESET_ALL}", rate = word_speed)
                pywriter.write(f"\nYou have {c.Fore.YELLOW}{game.max_hints - game._hints_used}{c.Style.RESET_ALL} hints remaining", rate = word_speed)
            else:
                pywriter.write(f"\n{c.Fore.RED}No hints remaining.{c.Style.RESET_ALL}", rate = word_speed)

        elif letter == "!":
            guess = input("\nMake a guess for the game: ").upper()
            if guess == game.secret_word:
                pywriter.write(f"{c.Fore.GREEN}\nCongrats! The word was {c.Fore.MAGENTA}{game.secret_word}{c.Style.RESET_ALL}", rate = word_speed)
                exit()
            
            elif game.guesses_used >= game.max_guesses:
                pywriter.write(f"{c.Fore.RED}\nOut of guesses :({c.Style.RESET_ALL}", rate = word_speed)
                exit()

            else:
                game.guesses_used += 1
                pywriter.write(f"{c.Fore.RED}Incorrect.{c.Style.RESET_ALL} You have {c.Fore.YELLOW}{game.max_guesses - game.guesses_used}{c.Style.RESET_ALL} guesses remaining", rate = word_speed)
                

        elif letter == ".":
            pywriter.write("\nGoodbye!")
            exit()
            
        elif letter == "*":
            print(game.__repr__())

        else:
            substitute = input(f"What letter do you want to replace '{letter}' with? ").strip()
            if game.change_letter(letter, substitute):
                pywriter.write(f"Congrats! The word was {game.secret_word}!", rate = word_speed)
                break
            else:
                print(f"\n{game}")

        if game.is_won():
            pywriter.write(f"{c.Fore.GREEN}Congrats! The word was {c.Fore.MAGENTA}{game.secret_word}{c.Style.RESET_ALL}", rate = word_speed)
        

        if game.is_lost():
            pywriter.write(f"{c.Fore.RED}You've used all your guesses. Game over!", rate = word_speed)
            pywriter.write(f"{c.Fore.GREEN}The correct phrase was: {c.Fore.MAGENTA}{game.secret_word}", rate = word_speed)

print(c.Style.RESET_ALL)