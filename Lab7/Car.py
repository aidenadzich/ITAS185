from Vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, colour, manufacturer, model, top_speed, year, number_of_doors, is_electric):
        super().__init__(colour, manufacturer, model, top_speed, year)
        self.number_of_doors = number_of_doors
        self.is_electric = is_electric

    def accelerate(self, accelerate_amount=2):
        super().accelerate(accelerate_amount)

    def __str__(self):
        electric_status = "is electric" if self.is_electric else "is not electric"
        return f"{super().__str__()} It has {self.number_of_doors} doors and {electric_status}."
    
if __name__ == "__main__":

    car1 = Car("Black", "Honda", "Civic", 200, 2012, 4, False)
    car1.accelerate()
    print(car1)