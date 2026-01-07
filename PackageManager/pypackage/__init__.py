class Bank:
    def __init__(self):
        self._amount = 100000        
        print(f"Total amount of your bank account: {self._amount}")
    
    def get_withdraw(self, amt):
        new_balance = self._amount - amt
        
        if new_balance < 0:
            print("Insufficient balance.")
        
        self._amount = new_balance
        print(f"Withdraw amount: {amt}\nYour Current balance: {self._amount}")

        return "Thank you!"