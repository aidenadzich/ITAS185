from Car import Car

class SportsCar(Car):

    def __init__(self, colour, manufacturer, model, top_speed, year, number_of_doors, is_electric):
        super().__init__(colour, manufacturer, model, top_speed, year, number_of_doors, is_electric)

    def accelerate(self):
        return super().accelerate(4)
    
if __name__ == "__main__":

    sports_car1 = SportsCar("White", "Porsche", "Taycan Turbo S", 257, 2019, 4, True)
    sports_car1.accelerate()
    print(sports_car1)