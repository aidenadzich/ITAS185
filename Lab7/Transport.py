from Vehicle import Vehicle

class Transport(Vehicle):

    def __init__(self, colour, manufacturer, model, top_speed, year, payload):
        super().__init__(colour, manufacturer, model, top_speed, year)
        self.payload = payload

    def accelerate(self):
        return super().accelerate(1)
    
    def __str__(self):
        return f"{super().__str__()} It can carry a payload of {self.payload} tons."
    
if __name__ == "__main__":

    transport1 = Transport("Red", "Peterbilt", "579", 120, 2012, 41)
    transport1.accelerate()
    print(transport1)