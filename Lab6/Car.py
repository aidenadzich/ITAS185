class Car:

     def __init__(self, model_year, make, speed = 0):
        self.model_year = model_year
        self.make = make
        self.speed = speed

     def __str__(self):
         return f"The {self.model_year} {self.make} is going {self.speed} kph"
     
     def accelerate(self):
         self.speed += 5
         print(self.__str__())

     def brake(self):
         self.speed -= 5
         if self.speed < 0:
             self.speed = 0
         self.__str__()
         print(self.__str__())
