from classes.Whale import Whale

class Humpback(Whale):

    def __init__(self, name, age, weight, fluke_width):
        super().__init__(name, age, weight)
        self.fluke_width = fluke_width

    def __str__(self):
        return super().__str__() + f", Fluke Width: {self.fluke_width}"
    
    def __eq__(self, other):
        if isinstance(other, Humpback):
            return super().__eq__(other) and self.fluke_width == other.fluke_width
        else:
            return False
        
    def sing(self):
        return f"Midtones and coos"
    
    def eat(self, food):
        print(f"Humpbacks eat lots and lots of {food}")