'''
AIDEN A - TEST 2 Q3 - ITAS185
'''

class Bread:

    '''
    Defines the attributes of bread
    '''
    def __init__(self, bread_type = 'white', quantity = 0, price_per_loaf = 5.25):
        self.bread_type = bread_type
        self.quantity = quantity
        self.price_per_loaf = price_per_loaf

    '''
    Adds the specified amount to the total quantity of bread
    '''
    def restock(self, amount):
        self.quantity += amount
        return self.quantity

    '''
    Removes the specified amounts from the total quantity of bread (if there is enough) and tells you the total cost
    '''
    def sell(self, amount):
        if amount < self.quantity:
            self.quantity -= amount
            total_cost = amount * self.price_per_loaf
            print(f"{amount} loaves of {self.bread_type} will cost you {total_cost:.2f}")
            return self.quantity, total_cost
        else:
            return -1
    
    '''
    Displaus the quanity, type, and price of bread
    '''
    def __str__(self):
        return f"{self.quantity} loaves of {self.bread_type} selling at {self.price_per_loaf:.2f} dollars a loaf."