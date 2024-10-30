class Dog:

    num_dogs = 0

    def __init__(self, name, age = 0, birth_year = 1970, breed = 'mutt', colour = 'mixed'):
        self.name = name
        self.age = age
        self.birth_year = birth_year
        self.breed = breed
        self.colour = colour
        Dog.num_dogs += 1

    def __str__(self):
        return f'{self.name} is a {self.age} year old {self.colour} {self.breed}'
    
    def __repr__(self):
        return print(f'{self.name} says bark')

    def speak(self):
        print(f"{self.name} says bark")
    
    def play(self, count):
        for i in range(count):
            print("Fetch ball")
            print("Beg for more")

    def eat(self, quantity, frequency):
        print(f"{self.name} is fed {frequency} times a day {quantity} of food")