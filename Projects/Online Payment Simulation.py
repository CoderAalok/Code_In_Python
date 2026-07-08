"""
Online Payment Features:
1) New account open
2) Sender & Receiver
3) Check main balance
4) Show statement

[Send] -> [Processing] -> [Receive]
"""

# Library
from pathlib import Path
from datetime import datetime
import json
import hashlib

# Config
BASE = Path(__file__).parent
USER_RECORD  = BASE / "user_record.json"


class OnlineSystem:
    def __init__(self):
        self.__records = loadRecord()
    
    # track user
    def find_user(self, phone_number):
        if not self.__records:
            return None
        
        for record in self.__records:
            if record["Phone No."] == phone_number:
                return record
        return None
    
    # save updated record
    def update_record(self):
        updateRecord(self.__records)
    
    # encode pin
    def hash_pin(self, pin):
        return hashlib.sha256(pin.encode()).hexdigest()
    
class OnlinePayment:
    def __init__(self, sendernumber, receivernumber, sender_pin, amount=0.0):
        self._snumber = sendernumber
        self._rnumber = receivernumber
        self.__pin = sender_pin
        self._amount = amount
        self.system = OnlineSystem()
        self.date = datetime.today().ctime()

    # check both sender and receiver have accounts
    @property
    def checkValidate(self):
        # fetch records
        sender_record = self.system.find_user(self._snumber)
        receiver_record = self.system.find_user(self._rnumber)
        
        # check sender have account
        if not sender_record:
            return f"User (+977-{self._snumber}) not found."
        
        if sender_record['PIN'] != self.system.hash_pin(self.__pin):
            return "Incorrect PIN."
        
        # check receiver have account 
        if not receiver_record:
            return f"User (+977-{self._rnumber}) not found."
        
        if sender_record['Phone No.'] == receiver_record['Phone No.']:
            return "Sender and receiver cannot be same."
        
        return self.transferMoney(sender_record, receiver_record)
        
    def transferMoney(self, sender_record, receiver_record):
        # sender sent money
        if self._amount > sender_record['Balance']:
            return "Insufficient balance."
        
        # subtract money from sender
        sender_record['Balance'] -= self._amount
        sender_record['Statement'].append(f"You sent Rs. {self._amount} on +977-{self._rnumber} account on {self.date}.")
        
        # add money to receiver
        receiver_record['Balance'] += self._amount 
        receiver_record['Statement'].append(f"You received Rs. {self._amount} from +977-{self._snumber} account on {self.date}.")
        
        # update and save
        self.system.update_record()
        
        return "Payment successful."


# balance check
class BalanceCheck:
    def __init__(self, usernumber):
        self._number = usernumber
        self.system = OnlineSystem()
    
    @property
    def checkBalance(self):
        record = self.system.find_user(self._number)
        if not record:
            return "User not found."
        
        return f"Your main balance is Rs. {record['Balance']:.2f}."
        

# show statement  
class Statement:
    def __init__(self, usernumber):
        self._number = usernumber
        self.system = OnlineSystem()
        
    
    @property
    def showStatement(self):
        record = self.system.find_user(self._number)
        if not record:
            return ["User not found."]
        
        return record['Statement']


# New account verification
class Verification:
    def __init__(self, username, phonenumber, pin, balance=0.0):
        self.user = username
        self._number = phonenumber
        self.__pin = pin
        self._balance = balance
        self.statement = []
        self.number_size = 10 # maximum
        self.pin_size = 4 # maximum
        self.system = OnlineSystem()
        
    # create new account
    @property
    def createAccount(self):
        # check already using this number account created
        record = self.system.find_user(self._number)
        
        if record:
            return "Account already exist."

        # check username
        if not self.user.isalpha():
            return "Invalid UserName."
        
        # check phone number
        if (not self._number.isnumeric() or len(self._number) != self.number_size):
            return "Invalid phone number."
        
        # check PIN
        if (not self.__pin.isnumeric() or len(self.__pin) != self.pin_size):
            return "Invalid PIN."
        
        # record formate
        record = {
            "UserName": self.user,
            "Phone No.": self._number,
            "Balance": self._balance,
            "PIN": self.system.hash_pin(self.__pin),
            "Statement": self.statement
        }
        
        return saveRecord(record)


# Load record
def loadRecord():
    try:
        with open(USER_RECORD)as fr:
            return json.load(fr)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []


# Update and  Write records
def updateRecord(records):
    with open(USER_RECORD, 'w')as fw:
        json.dump(records, fw, indent=4)    


# save new account record
def saveRecord(record):
    # load record
    records = loadRecord()
    records.append(record)
    # update record
    updateRecord(records)
    return "Successfully! your account has been created."
    

def main(user_choice):
    if user_choice == "1":
        username = input("Enter your name:  ").strip()
        number = input("Enter your phone number: +977-").strip()
        pin = input("Create your PIN must be 4-digits: ").strip()
        
        user = Verification(username, number, pin)
        print(user.createAccount)
         
    elif user_choice == "2":
        sender_number = input("Sender number: +977-").strip()
        receiver_number = input("Receiver number: +977-").strip()
        
        try:
            amount = float(input("Amount: ").strip())
        except ValueError:
            print("Invalid amount.")
            return
            
        pin = input("Enter your PIN: ").strip()
        
        pay = OnlinePayment(sender_number, receiver_number, pin, amount)
        print(pay.checkValidate)
    
    elif user_choice == "3":
            user_number = input("User number: +977-").strip()
            balance = BalanceCheck(user_number)
            print(balance.checkBalance)
    
    elif user_choice == "4":
        user_number = input("User number: +977-").strip()
        statement = Statement(user_number)
        print("\n".join(statement.showStatement))
    
    else:
        print("Only select (1-5).")


# Test
if __name__ == "__main__":
    print("=-=-=-=-=-= Online Payment Simulation =-=-=-=-=-=-=")
    
    while True:
        print("1) Create new account")
        print("2) Send/Payment/Transfer")
        print("3) Check main balance")
        print("4) Show statement")
        print("5) Exit")
        
        user_choice = input("\nSelect any one (1-5): ").strip()
        if user_choice == "5":
            print("See you later.")
            break
        main(user_choice)
