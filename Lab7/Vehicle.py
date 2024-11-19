class Vehicle:

    def __init__(self, colour, manufacturer, model, top_speed, year):
        self.colour = colour
        self.manufacturer = manufacturer
        self.model = model
        self.speed = 0
        self.top_speed = top_speed
        self.year = year

    def accelerate(self, accelerate_amount = 3):
        self.speed += accelerate_amount
        if self.speed > self.top_speed:
            self.speed == self.top_speed
        
    def brake(self, brake_amount = 2):
        self.speed -= brake_amount
        if self.speed < 0:
            self.speed = 0

    def __str__(self):
        return f"{self.year} {self.colour} {self.manufacturer} {self.model} is travelling {self.speed} kph with a maximum speed of {self.top_speed} kph."
    
    def __eq__(self, other):
        if isinstance(other, Vehicle):
            return (self.top_speed == other.top_speed and
                    self.manufacturer == other.manufacturer and
                    self.year == other.year)
        return False
    
if __name__ == "__main__":

    vehicle1 = Vehicle("Silver", "Honda", "Prelude", 180, 1999)
    vehicle1.accelerate(10)
    vehicle1.brake(5)
    print(vehicle1)