import classes.Vehicle as v

class Car(v.Vehicle):
    def vroom(self):
        print('Vrooooom')
    
    def start_engine(self):
        print(f'Starting the engine of {self.make} {self.model} car')
        