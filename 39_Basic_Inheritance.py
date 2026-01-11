# Level 1
# Question-1

# class Animal:
#     def sound(self):
#         print("Animals sounds likes...")

# class Dog(Animal):
#     def sound(self):
#         print("Dogs: Dogs sounds likes Boow boow!")

# class Cat(Animal):
#     def sound(self):
#         print("Cats: Cats sounds likes Meow meow!")

# dog = Dog()
# dog.sound()
# cat = Cat()
# cat.sound()
# ------------------------------------------------------------

#Question-2

# class Vehicle:
#     def __init__(self,max_speed):
#         self.s = max_speed
    
# class Car(Vehicle):
#     def __init__(self,max_speed, brand):
#         super().__init__(max_speed)  #Check max_speed is it or not and call Vehicle constructor
#         self.b = brand
        
  
# car = Car("400km/hr","Roll's Royce")
# c = Car("300km/hr","Audi")
# print(f"Top Speed: {car.s}, {c.s}")
# print(f"Car Brand: {car.b}, {c.b}")

# Question-3

# class Person:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
# class Student(Person):
#     def __init__(self,name,age,roll_no):
#         super().__init__(name,age)
#         self.roll_no = roll_no
    
#     # All details
#     def get_detail(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Roll_no: {self.roll_no}")
        
# name = input().title()
# age,roll_no = map(int,input().split())

# detail = Student(name,age,roll_no)   
# detail.get_detail()

# # Question-4
# class Parent:
#     def display(self):
#         print("Parent: We have a child.")
    
# class Child(Parent):
#     pass

# child = Child()
# child.display()

# Level-2
# Question:5
# class A:

#     def __init__(self):
#         print("A called")

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("B called")

# class C(B):
#     def __init__(self):
#         super().__init__()
#         print("C called")

# call = C()


# Question:7
# class Employee:
#     # Inshort about Employee
#     def __init__(self,name,company):
#         self.name = name
#         self.company = company
    
#     def calc_salary(self,netsalary):
#             return netsalary

# class FullTimeEmployee(Employee):

#         def __init__(self,name,company,salary,bonus,rate,tax):
#             super().__init__(name,company)
#             self.salary = salary
#             self.bonus = bonus
#             self.rate = rate
#             self.tax = tax

#         def calc_salary(self):
#             total_salary = self.salary*self.rate+self.bonus - self.tax
#             return total_salary

# class PartTimeEmployee(Employee):
#         def __init__(self,pay,time):
#             self.hourly = pay
#             self.working_duration = time
        
#         def calc_salary(self):
#             if self.working_duration > 12:
#                 totalsalary = self.hourly*(self.working_duration)//60
#                 return totalsalary 
#             else:
#                 totalsalary = self.hourly*self.working_duration
#                 return totalsalary       
        
# # ---Main Program---
# # About Employee
# name = input().title().strip()
# company = input().title().strip()

# # Income for Full time
# #Salary of Employee
# salary = int(input("Salary: ").strip()) 

# # Deal by Manager 
# bonus = int(input("Add Bonus: ").strip())
# rate = int(input("Add rate%: ").strip())  
# tax = int(input("Tax%: ").strip())

# # Income for Part time
# # Deal by Manager  
# hourly = int(input("Pay Hourly: "))
# # working time for Employee
# time = float(input("Time:  ").strip())

# # calling class
# full = FullTimeEmployee(name,company,salary,bonus,rate,tax)
# t1 = full.calc_salary()
# part = PartTimeEmployee(hourly,time)
# t2 = part.calc_salary()

# # Final result
# print(f"Name: {e.name}")
# print(f"Working on: {e.company}")
# print(f"Salary: {e.calc_salary(t1+t2)}")




# class Employee:
#     def calc_salary(self):
#         pass

# class FullTimeEmployee(Employee):
#     def __init__(self,salary,bonus):
#         self.salary = salary
#         self.bonus = bonus
        
#     def calc_salary(self):
#         return self.salary+self.bonus
    
# class PartTimeEmployee(Employee):
#     def __init__(self,hours,rate):
#         self.hours = hours
#         self.rate = rate
    
#     def calc_salary(self):
#         return self.hours*self.rate

# salary = int(input().strip())
# bonus = int(input().strip())

# hours = int(input().strip())
# rate = int(input().strip()) 

# full = FullTimeEmployee(salary,bonus)
# part = PartTimeEmployee(hours,rate)

# print(f"Full time Employee salary: {full.calc_salary()}")
# print(f"Part time Employee salary: {part.calc_salary()}")



# Queation: 8
class BankAccount:
    def __init__(self,balance=2000.09):
        self.balance = balance

    def withdraw(self,drawAmount):
        if drawAmount>self.balance:
            return ("Out of range main balance")
        else:
            self.balance -= drawAmount
            return drawAmount,self.balance

class SavingsAccount(BankAccount):
    def __init__(self,balance=5000.89):
        super().__init__(balance)
            
    def withdraw(self,drawAmount):
        if drawAmount>self.balance:
            raise ValueError("Out of range main balance")
        else:
            self.balance -= drawAmount
            return drawAmount,self.balance

Bank = BankAccount()
Saving = SavingsAccount()

# For BankAccount
try:
    drawAmount,balance = Bank.withdraw(200)
    print(f"Successfully withdraw from Bank Account Rs. {drawAmount}")
    print(f"Now current balance is Rs. {balance:.2f}\n")
    print()
    drawAmount,balance = Bank.withdraw(12200)
    print(f"Successfully withdraw from Bank Account Rs. {drawAmount}")
    print(f"Now current balance is Rs. {balance:.2f}\n")
except ValueError :
    print("Out of range main balance")

# For SavingAccount
try:
    drawAmount,balance = Saving.withdraw(2000)
    print(f"Successfully withdraw from Saving Account Rs. {drawAmount}")
    print(f"Now current balance is Rs. {balance:.2f}")
except ValueError :
    print("Out of range main balance")
