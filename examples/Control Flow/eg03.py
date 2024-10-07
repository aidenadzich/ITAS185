'''
    Example of if-elif-else combination
'''

food = 'spam'

if food.lower == 'spam':
    
    print("Yum My Favourite")
    print("I feel like saying it 100 times")
    print(10 * (food + "! "))

elif food == 'bacon':

    print("I prefer bacon and eggs")
    print("I don't like spam")
elif food == 'tacos':
    print("It's taco tuesday!")
elif food == 'pancakes':
    print("Pancakes aren't just for breakfast!")
else:
    print("I want something different")
print("The meal is over")