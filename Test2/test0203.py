'''
AIDEN A - TEST 2 Q3 - ITAS185
'''

import Bread as b


'''
Creates objects
'''
b1 = b.Bread('Whole Wheat', 10, 6.0)
b2 = b.Bread('White', 15, 5.25)
b3 = b.Bread('Sourdough', 0, 6.5)

print(f"There are {b1.quantity} loaves of {b1.bread_type}, {b2.quantity} loaves of {b2.bread_type}, and {b3.quantity} loaves of {b3.bread_type}")

'''
Calls method to restock the object amounts
'''
b1.restock(5)
b2.restock(2)
b3.restock(20)

print(f"There are {b1.quantity} loaves of {b1.bread_type}, {b2.quantity} loaves of {b2.bread_type}, and {b3.quantity} loaves of {b3.bread_type} after restocking them all")

'''
Calls method to reduce the quantity of the object, and display a total cost
'''
b1.sell(2)
b2.sell(6)
b3.sell(10)

print(f"There are {b1.quantity} loaves of {b1.bread_type}, {b2.quantity} loaves of {b2.bread_type}, and {b3.quantity} loaves of {b3.bread_type} after selling some")

'''
Calls a method to tell us the quantity, type of bread, and sale price
'''
print(b1)
print(b2)
print(b3)