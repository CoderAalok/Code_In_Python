#Question_6
# class Book:
#     def __init__(self,title,author,price,name):
#         self.title = title
#         self.author = author
#         self.price = price 
#         self.name = name
#         print(f"Name of Book: {self.name}")
#         print(f"Title: {self.title}")
#         print(f"Author : {self.author}")
#         print(f"Price : {self.price}")
        
        
# name = input("Name of book: ").capitalize()
# title = input(f"What's title of {name} book: ")
# author = input(f"Who is the author of {name} book: ")
# price = int(input("How much: "))
# pustak = Book(name,title, author, price)

#Question_7
# class Employee:
#     # old_company_name = "Google"      #class attribute
#     # TechCorp = "Software Engineer"
#     # new = input("new company name: ")
#     def __init__(self,name , salary, old_company_name,TechCorp,new_company,contact ):   #Constroctor
#         self.name = name 
#         self.salary = salary
#         self.old = old_company_name
#         self.tech = TechCorp
#         self.new = new_company
#         self.conts = contact
#     def info(self):         #Instance Attribute
#         print("---------New Employee Informations-------")
#         print(f"Name: {self.name}")
#         print(f"Salary: {self.salary}")
#         print(f"Working On: {self.old} ")
#         print(f"TechCorp: {self.tech}")
#         print(f"Now joining: {self.new}")
#         print(f"Contact Number: {self.conts}")
#         print("----------------------------")

# name = input("Enter your Name: ")
# old_company_name =  input("Enter your old company name: ")
# TechCorp =  input("In which field you were work: ")
# new_company =  input("Enter your new company name where you need to work : ")
# salary = int(input("Enter your Salary: "))
# contact = (input("Enter your Contact Number: "))

# emp = Employee(name, salary, old_company_name,TechCorp,new_company,contact)
# emp.info()

#Queation_8
# # class Circle:
# #     def __init__(self,radius):
# #         self.r = radius
# #     def get_area(self):
# #         area= (22/7)* (self.r)**2
# #         print(f"The area of circle is {area: .2f}")
# #     def get_circumfrance(self):
# #         c = 2*(22/7)*(self.r)
# #         print(f"Circumfrance of circle is {c: .2f}")
# # sphere = Circle(5)
# # sphere.get_area()
# # sphere.get_circumfrance()
        
# #Question_9 (Second hand Laptop sell)
# class Laptop:
#     def __init__(self,model,processor,ram, rom, screen, backlit,finger,price):
#         self.model = model
#         self.Processor = processor
#         self.RAM = ram
#         self.ROM = rom
#         self.Screen = screen
#         self.Backlit = backlit
#         self.Finger = finger
#         self.price = price
#     def info(self):
#         print("------HERE Second hand Laptops With Exclusive Price-------")
#         print(f" Model: {self.model}")
#         print(f"Processor: {self.Processor}")
#         print(f"RAM: {self.RAM}")
#         print(f" ROM: {self.ROM}") 
#         print(f"SCREEN: {self.Screen}") 
#         print(f"Bakelit: {self.Backlit}") 
#         print(f" Finger: {self.Finger}")
#         print(f"Price: {self.price}")

# # model = input("Model: ")
# # processor = input("Processor:")
# # ram = input("RAM: ")
# # rom = input("ROM: ")
# # screen = input("SCREeN: ")
# # backlit = input("Backlit: ")
# # finger = input("Finger: ")
# # price = int(input("Price: "))
# hardware = Laptop(model,processor,ram, rom, screen, backlit,finger,price)

#Question_10 
# class Temperature:
#     def __init__(self, celsius, fahrenheit):
#         self.C = celsius
#         self.F = fahrenheit
#     def get_Celsius(self):
#         celsius = (self.F - 32)* 5/9
#         print(f"{self.F}°F to {self.C}°C: {celsius:.2f}°C")
#     def get_Fahrenheit(self):
#         Fahrenheit = (9/5 * self.C)+32
#         print(f" {self.C}°C to {self.F}°F : {Fahrenheit: .2f}°F")
# temp = Temperature(40,212)
# temp.get_Celsius()  #Temperature.get_Celsius(temp)
# temp.get_Fahrenheit()  #Temperature.get_Fahrenheit(temp) 


#BankAccount Simulator
import captcha
class Account:
    def __init__(self):
        self.balance = 0.0

    def get_deposit(self):

        while True:
            try:
                deposit = float(input("How much do you need to deposit? >> "))
            except ValueError:
                print("❌ Invalid input. Please tryagain!")
                continue

            if deposit <= 0:
                print("❌ Invalid input. Please tryagain!")
                continue

            self.balance += deposit
            print("--------------------------------------")
            print(f"Successully deposit Rs.{deposit}.")
            print("--------------------------------------")
            print(f"Your Current balance is Rs.{self.balance}.")
            print("--------------------------------------")
            break

    def get_withdraw(self):
        i = 1
        max_time = 5
        while i <= max_time:
            try:
                withdraw = int(input("How much do you want to withdraw? >> "))
            except ValueError:
                print("❌ Invalid input. Please tryagain!")
                i += 1
                continue

            if withdraw > self.balance:
                print("⚠️ Insufficient your bank balance!")
                i += 1
                continue
            
            if withdraw < 1000:
                print("⚠️ Minimum money must be Rs.1000+ ")
                i += 1
                continue

            self.balance -= withdraw
            print("--------------------------------------")
            print(f"\n✅Successfully Withdraw Rs.{withdraw}.")
            print("--------------------------------------")
            print(f"Your current bank balance: Rs.{self.balance}.")
            print("--------------------------------------")
            return True

        if i > max_time:
            print("\n Multiple attempt! your account temporarily paused!")
        return False
    
    def get_balance(self):
        print("--------------------------------------")
        print(f"🏦Your current bank balance is {self.balance}.")
        print("--------------------------------------")

Encryption = {}
while True:
    name = input("Your Name: ")  # key
    if  not name :
        print("Name required!")
        continue
    break

while True:
    account_no = (input("Your Account_No.: "))  #value

    if len(account_no) != 16 or not account_no.isdigit():
            print("Account No. must be 16-digits...")
            continue
    break
while True:
    pin = (input("Your PIN-Code: "))  #value
    if len(pin) != 4 or not pin.isdigit():
            print("PIN Code must 4-digits...")
            continue
    break

Encryption[name] = ["Account_No.:",account_no,"PIN Code:",pin]
while True:
    confirm = input(f"Are you sure about your info: Name:{Encryption} (Yes/No) ").lower()
    if confirm == '' or not isinstance(confirm,str) :
         print("Either (Yes/No) only.")
         continue
    break

if confirm == 'yes':
    while True:
        Captcha = captcha.captcha_gen()
        captcha_verification = input(f"To fill this captcha '{Captcha}' -->>: ")
        if captcha_verification == '' or captcha_verification != Captcha:
            print("Must fill correctly...")
            continue
        break

    print("Successfully your account open.......")
    bank = Account()

    while True:
        try:
            user = int(input("What do you want:\n 1.Balance Check\n 2.Deposit\n 3.Withdraw\n 4.Exit ----> "))
        except ValueError:
            print("Invaild input!")
            continue

        if user == 1:
            bank.get_balance()
            continue

        elif user == 2:
            bank.get_deposit()
            bank.get_balance()
            continue

        elif user == 3:
           if bank.get_withdraw():
                bank.get_balance()
           continue

        elif user == 4:
            print("Thanks for Banking with us!")
            break

        else:
            print("Out of range! Pick: 1-4")
            continue

else:
    print("Make ensure your information and re-input!")
