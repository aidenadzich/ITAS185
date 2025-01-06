from abc import abstractmethod

class Whale():

    count = 0

    def __init__(self, name, age, weight):
        self.name = str(name)
        self.age = int(age)
        self.weight = float(weight)
        Whale.count += 1

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}"
        
    def __eq__(self, other):
        return self.age == other.age and self.name == other.name and self.weight == other.weight

    @abstractmethod
    def sing(self):
        pass

    @abstractmethod
    def eat(self, food):
        pass



