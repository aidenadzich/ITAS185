from classes.Whale import Whale

class Orca(Whale):
    
    def __init__(self, name, age, weight, pod):
        super().__init__(name, age, weight)
        self.pod = pod
        self.count = Whale.count

    def __str__(self):
        return super().__str__() + f", Pod: {self.pod}"
    
    def __eq__(self, other):
        return super().__eq__(other) and self.pod == other.pod
        
    def sing(self):
        return f"High chirps and trills"
    
    def eat(self, food):
        print(f"Orcas eat meat like {food}")