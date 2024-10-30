import datetime as dt

class Animal():
    animal_count = 0
    
    def __init__(self, name="", yob=0, is_vegetarian=False):
        self.name = name
        self.yob = yob
        self.is_vegetarian = is_vegetarian
        Animal.animal_count += 1
    
    def speak(self):
        pass
    
    def eat(self, food):
        print(f"{self.name} is eating {food}")

    def drink(self, drink):
        print(f"{self.name} is drinking {drink}")
    
    def get_age(self):
        return dt.datetime.now().year - self.yob
    
    def __str__(self):
        return f"{self.name} is a {self.get_age()} year old {self.__class__.__name__}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.yob!r}, {self.is_vegetarian!r})"
    