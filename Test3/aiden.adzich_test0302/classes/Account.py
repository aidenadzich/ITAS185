class Account:

    def __init__(self, owner = "", start_amount = 0):
        self.owner = str(owner)
        try:
            self.start_amount = start_amount
            
            if not isinstance(start_amount, (int)) or start_amount <= 0:
                raise TypeError(f"Starting amount must be a positive integer, {self.start_amount} received")
            
            if owner == "":
                raise TypeError("Owner must be passed and cannot be empty!")
            
        except TypeError as e:
            print(e)

        self._transactions = []

    def __str__(self):
        return f"Account of {self.owner} with starting amount {self.start_amount}"
    
    def add_transaction(self, amount):
        try:
            if isinstance(amount, (int)):
                self._transactions.append(amount)
            else:
                raise ValueError("Please use an integer amount")
        except ValueError as e:
            print(e)

    @property
    def balance(self):
        return self.start_amount + sum(self._transactions)
    
    def __len__(self):
        return len(self._transactions)

    