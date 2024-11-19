from Car import Car

class Pickup(Car):

    def __init__(self, colour, manufacturer, model, top_speed, year, number_of_doors, is_electric):
        super().__init__(colour, manufacturer, model, top_speed, year, number_of_doors, is_electric)

    def accelerate(self):
        return super().accelerate(1.5)
    

if __name__ == "__main__":
    
    pickup1 = Pickup("Grey", "Chevrolet", "Silverado", 190, 2013, 4, False)