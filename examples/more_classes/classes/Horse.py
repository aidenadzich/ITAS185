import classes.Animal as a

class Horse(a.Animal):
    def __init__(self, name="", yob=0, is_vegetarian=False, height=0):
        super().__init__(name, yob, is_vegetarian)
        self.height = height

    def speak(self):
        print(f'{self.name} says neigh')
