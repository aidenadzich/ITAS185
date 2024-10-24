import random

ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

deck = [rank + ' of ' + suit for rank in ranks for suit in suits]
print(deck)

random.shuffle(deck)
print(deck)