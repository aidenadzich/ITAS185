from abc import ABC, abstractmethod
# Define an abstract base class (ABC) representing a Vehicle
class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def honk_honk(self):
        print('Honk Honk')

    @abstractmethod
    def start_engine(self):
        pass