from Vehicle import Vehicle
from Car import Car
from Transport import Transport
from Pickup import Pickup
from SportsCar import SportsCar

print("\nTest Car Class")

print("\nCar 1 Test:")
car1 = Car("Black", "Honda", "Civic", 180, 2012, 4, False) #Create Car 1
car1.accelerate(200) #Test Car 1 Acceleration. Will no go above top speed
print(car1)
car1.brake(20) #Test Car 1 Braking
print(car1)

print("\nCar 2 Test:")
car2 = Car("Silver", "Honda", "Prelude", 225, 1999, 2, False) #Create Car 2
car2.accelerate(60) #Test Car 2 Acceleration
print(car2)
car2.brake(65) #Test Car 2 Braking. Will not go below 0 kph
print(car2) 

print("\n\nTest Transport Class")

print("\nTransport 1 Test:")
transport1 = Transport("Red", "Peterbilt", "579", 120, 2012, 41)
transport1.accelerate()
print(transport1)

print("\nTransport 2 Test:")
transport2 = Transport("Red", "Mack", "Super-Liner Sleeper", 150, 1985, 90)
transport2.accelerate()
transport2.accelerate()
print(transport2)

print("\n\nTest Pickup Class")

print("\nPickup 1 TestL")
pickup1 = Pickup("Grey", "Chevrolet", "Silverado 2500", 190, 2013, False)
pickup1.accelerate()
print(pickup1)
pickup1.brake(5)
print(pickup1)