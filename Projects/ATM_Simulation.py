class BankAccount:
    def __init__(self):
        self.balance = 0.0
    def get_deposit(self):
        while True:
            deposit = float(input("How much do you need to deposit? >> "))
            if deposit <= 0:
                print("❌Invalid input. Please tryagain!")
                continue
            self.balance += deposit
            print("--------------------------------------")
            print(f"Successully! deposit Rs.{deposit}.")
            print("--------------------------------------")
            print(f"Now your Current balance is {self.balance}.")
            print("--------------------------------------")
            break
        
    def get_withdraw(self):
        while True:
            withdraw = int(input("How much do you want to withdraw? >> "))
            if withdraw <= 0 or withdraw > self.balance:
                print("⚠️Insufficient your bank balance!")
                continue
            self.balance -= withdraw
            print("--------------------------------------")
            print(f"\n✅Successfull! Withdraw Rs.{withdraw}.")
            print("--------------------------------------")
            print(f"Now your current bank balance: {self.balance}.")
            print("--------------------------------------")
            break
        
    def balance_check(self):
        print("--------------------------------------")
        print(f"🏦Your current bank balance is {self.balance}.")
        print("--------------------------------------")

bank = BankAccount()
bank.balance_check()
bank.get_deposit()
bank.get_withdraw()
bank.balance_check()