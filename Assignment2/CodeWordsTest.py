import random
import string

class CodeWordsGame:
    def __init__(self):
        # Initialize the game by selecting a word, encoding it, and setting initial game parameters
        self.secret_word = self.select_word().upper()  # The original word/phrase in upper case
        self.coded_word = self.mix_word(self.secret_word)  # The encoded version of the secret word
        self.max_hints = 3  # Maximum number of hints allowed
        self._hints_used = 0  # Private attribute to track the number of hints used

    def read_file(self):
        # Reads the file 'codewords.txt' and returns a list of words/phrases
        with open('codewords.txt', 'r') as file:
            return [line.strip() for line in file.readlines()]  # Remove newline characters and return list of phrases

    def select_word(self):
        # Selects a random word/phrase from the list read from the file
        words = self.read_file()
        return random.choice(words)  # Choose a random phrase from the list

    def encode_word(self, word):
        # Encodes the selected word/phrase by substituting its letters with a shuffled alphabet
        mixed_alphabet = ''.join(random.sample(string.ascii_uppercase, len(string.ascii_uppercase)))  # Randomly shuffle the alphabet
        self.encoding_map = str.maketrans(string.ascii_uppercase, mixed_alphabet)  # Create a translation map for encoding
        self.decoding_map = str.maketrans(mixed_alphabet, string.ascii_uppercase)  # Create a translation map for decoding
        return word.translate(self.encoding_map)  # Return the encoded word/phrase

    def mix_word(self, word):
        # Mixes the word using a random substitution cipher
        mixed_alphabet = ''.join(random.sample(string.ascii_uppercase, len(string.ascii_uppercase)))  # Randomly shuffle the alphabet
        self.encoding_map = str.maketrans(string.ascii_uppercase, mixed_alphabet)  # Create a translation map for encoding
        self.decoding_map = str.maketrans(mixed_alphabet, string.ascii_uppercase)  # Create a translation map for decoding
        return word.translate(self.encoding_map)  # Return the encoded word/phrase

    def make_guess(self, letter, substitute):
        # Processes a guess by replacing a letter in the coded word with a guessed letter
        letter = letter.upper()  # Ensure the input letter is uppercase
        substitute = substitute.upper()  # Ensure the substitute letter is uppercase
        if letter in self.coded_word and substitute.isalpha() and len(substitute) == 1:  # Validate the input
            self.coded_word = self.coded_word.replace(letter, substitute)  # Replace the letter in the coded word
            return self.coded_word == self.secret_word  # Check if the guess solves the puzzle
        else:
            return False  # Return False if the input is invalid or does not solve the puzzle

    def get_hint(self):
        # Provides a hint by substituting a random letter in the coded word with its correct match from the secret word
        if self._hints_used < self.max_hints:  # Check if there are hints remaining
            random_letter = random.choice([c for c in self.coded_word if c.isalpha()])  # Choose a random letter from the coded word
            decoded_letter = random_letter.translate(self.decoding_map)  # Find the corresponding letter in the original word
            self.coded_word = self.coded_word.replace(random_letter, decoded_letter)  # Replace the letter in the coded word
            self._hints_used += 1  # Increment the count of hints used
            return random_letter, decoded_letter  # Return the letter and its substitution
        else:
            return None  # Return None if no hints are left

    def is_won(self):
        # Checks if the game is won (i.e., the coded word matches the secret word)
        return self.coded_word == self.secret_word

    def is_lost(self):
        # Checks if the game is lost (i.e., all hints have been used up)
        return self._hints_used >= self.max_hints

    def __str__(self):
        # Returns a string representation of the coded word for display
        return f'Coded Word: {self.coded_word}'

    def __repr__(self):
        # Returns a detailed representation of the object for debugging
        return f'CodeWordsGame(secret_word={self.secret_word}, coded_word={self.coded_word}, max_hints={self.max_hints}, hints_used={self._hints_used})'

    def __eq__(self, other):
        # Checks equality between two CodeWordsGame objects based on the secret word
        return self.secret_word == other.secret_word

# Example of how to run the game
if __name__ == "__main__":
    game = CodeWordsGame()  # Create a new instance of CodeWordsGame
    print("Welcome to CodeWords. I have encoded a phrase as:")
    print(game)  # Display the coded word
    print(game.secret_word)
    print(f"\nYou may get a random hint by specifying ? when prompted for a letter. You have {game.max_hints - game._hints_used} hints remaining\n")

    # Main game loop
    while not game.is_won() and not game.is_lost():
        letter = input("What letter do you want to substitute? ").strip()  # Prompt user for a letter to replace
        if letter == "?":  # Check if the user requested a hint
            hint = game.get_hint()  # Get a hint
            if hint:
                print(f"I will substitute {hint[0]} for {hint[1]}. Now your phrase is:")
                print(game)  # Display the updated coded word
                print(f"\nYou have {game.max_hints - game._hints_used} hints remaining\n")
            else:
                print("No hints remaining.")  # Inform the user if no hints are left
        else:
            substitute = input(f"What letter do you want to replace '{letter}' with? ").strip()  # Prompt for the substitute letter
            if game.make_guess(letter, substitute):  # Make the guess and check if it solves the puzzle
                print("Congratulations! You've guessed the phrase correctly.")
                break  # Exit the loop if the game is won
            else:
                print(game)  # Display the current state of the coded word
                print("\nNot solved yet…\n")

    if game.is_lost():  # Check if the game is lost
        print("You've used all your hints. Game over!")
        print(f"The correct phrase was: {game.secret_word}")  # Reveal the correct phrase
