import Dog as d

my_dog = d.Dog('Sansa', 14, 2010, 'Australian Shepard', 'Blue Merl')

connor_dog = d.Dog('Phoebe', 7, 2017, 'Belgian Shepard', 'Black')

print(f'# of dogs: {d.Dog.num_dogs}')

my_dog.speak()
my_dog.play(1)
connor_dog.eat('2 cups', 3)

print(my_dog.name)
print(connor_dog.breed)
print(my_dog)
print(connor_dog)
print(repr(my_dog))