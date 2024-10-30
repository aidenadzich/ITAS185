import classes.Otter as o
import classes.Horse as h

animals = []
a4 = o.Otter('Otto', 2018, True, 5)
a5 = o.Otter('Oscar', 2019, False, 3)
a6 = h.Horse('Harry', 2006, True, 9)


animals.append(a4)
animals.append(a5)
animals.append(a6)

for animal in animals:
    print(animal)