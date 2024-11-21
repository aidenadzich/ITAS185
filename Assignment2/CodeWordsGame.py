import random
import string
import pywriter
import colorama

class CodeWordsGame:
    def __init__(self):
        self.secret_word = self.select_word().upper()
        self.coded_word = self.encode_word(self.secret_word)
        self.max_hints = 3
        self._hints_used = 0
        self.max_guesses = 3
        self.guesses_used = 0

    def read_file(self):
        with open('codewords.txt', 'r') as file:
            return [line.strip() for line in file.readlines()]

    def select_word(self):
        words = self.read_file()
        return random.choice(words)

    def encode_word(self, word):
        shuffled_alpha = ''.join(random.sample(string.ascii_uppercase, len(string.ascii_uppercase)))
        self.encoding_map = str.maketrans(string.ascii_uppercase, shuffled_alpha)
        self.decoding_map = str.maketrans(shuffled_alpha, string.ascii_uppercase)
        return word.translate(self.encoding_map)

    def change_letter(self, letter, substitute):
        letter = letter.upper()
        substitute = substitute.upper()

        if substitute in self.coded_word:
            print(f"The letter '{substitute}' has already been used in the coded word. Choose a different substitute.")
            return False
        
        if len(letter) > 1:
            print("You can only select one letter!")
            return False

        if letter.isalpha() and substitute.isalpha() and len(substitute) == 1:
            if letter in self.coded_word:
                self.coded_word = self.coded_word.replace(letter, substitute)
                return self.coded_word == self.secret_word
            else:
                print(f"The letter '{letter}' is not part of the original secret word.")
                return False
        else:
            print("Invalid input. Ensure you enter one valid letter for both fields.")
            return False


    def get_hint(self):
        if self._hints_used < self.max_hints:
            random_letter = random.choice([_ for _ in self.coded_word if _.isalpha()])
            decoded_letter = random_letter.translate(self.decoding_map)
            self.coded_word = self.coded_word.replace(random_letter, decoded_letter)
            self._hints_used += 1
            return random_letter, decoded_letter
        else:
            return None


    def is_won(self): 
        return self.coded_word == self.secret_word

    def is_lost(self):
        return self.guesses_used > self.max_hints

    def __str__(self):
        return f'Coded Word: {self.coded_word}'

    def __repr__(self):
        return f'CodeWordsGame(secret_word={self.secret_word}, coded_word={self.coded_word}, max_hints={self.max_hints}, hints_used={self._hints_used})'

    def __eq__(self, other):
        return self.secret_word == other.secret_word

if __name__ == "__main__":
    game = CodeWordsGame()
    word_speed = 0.02
    pywriter.write(f"Welcome to CodeWords. I have encoded a phrase as: {game.coded_word}", rate = word_speed)
    pywriter.write(f"\nEnter a letter to select it for replacement", rate = word_speed)
    pywriter.write(f"\nEnter '?' to use a hint. You have {game.max_hints} hints available to you", rate = word_speed)
    pywriter.write(f"\nEnter '!' to make a guess. You have {game.max_guesses} guesses. If you run out, game over!", rate = word_speed)
    print(game.secret_word)

    while not game.is_won() and not game.is_lost():
        letter = input("\nMake your selection: ").strip()
        if letter == "?":
            hint = game.get_hint()
            if hint:
                pywriter.write(f"\n{hint[0]} has been replaced with {hint[1]}. Now your phrase is:\n", rate = word_speed)
                pywriter.write(game.coded_word, rate = word_speed)
                pywriter.write(f"\nYou have {game.max_hints - game._hints_used} hints remaining", rate = word_speed)
            else:
                pywriter.write("No hints remaining.", rate = word_speed)

        elif letter == "!":
            guess = input("Make a guess for the game: ").upper()
            #game.guess_word(guess)
            if guess == game.secret_word:
                pywriter.write(f"\nCongrats! The word was {game.secret_word}!", rate = word_speed)
                exit()
            
            elif game.guesses_used >= game.max_guesses:
                pywriter.write("Out of guesses :(", rate = word_speed)
                exit()

            else:
                pywriter.write(f"Incorrect. You have {game.max_guesses - game.guesses_used} guesses remaining", rate = word_speed)
                game.guesses_used += 1
            

        else:
            substitute = input(f"What letter do you want to replace '{letter}' with? ").strip()
            if game.change_letter(letter, substitute):
                pywriter.write(f"Congrats! The word was {game.secret_word}!", rate = word_speed)
                break
            else:
                print(game)

        if game.is_won():
            pywriter.write(f"Congrats! The word was {game.secret_word}!", rate = word_speed)
        

        if game.is_lost():
            pywriter.write("You've used all your guesses. Game over!", rate = word_speed)
            pywriter.write(f"The correct phrase was: {game.secret_word}", rate = word_speed)
