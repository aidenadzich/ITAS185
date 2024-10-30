import classes.Animal as a
import classes.WingedAnimal as wa

class Bat(a.Animal, wa.WingedAnimal):
    def __init__(self, name, yob, is_vegetarian, wing_colour, eyesight="Good"):
        a.Animal.__init__(name, yob, is_vegetarian)
        wa.WingedAnimal.__init__(wing_colour)
        self.eyesight = eyesight

    def fly(self):
        print(f'The {self.wing_colour} bat flies')