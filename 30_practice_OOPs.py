# problem_1

# class Programmer:
#     company = "Microsoft"
#     def __init__(self,name,exp):
#         self.name = name
#         self.exp = exp
#     def getcode(self):
#         print(f"Name: {self.name} \n Experience: {self.exp} \n Working_ON: {self.company}")
# pro = Programmer("Jackie","2_years") #first 
# cal = Programmer('mick','1_year')  #second
# pro.getcode()
# cal.getcode()


#Programmer Details
# class Programmer:

#     def __init__(self,name, exp,company):
#         self.name = name
#         self.exp = exp
#         self.company = company

#     def worker(self): 
#         print(f" Name: {self.name}\n Experience: {self.exp}\n Working_ON: {self.company}")

# for i in range(1,3):
#     name = input("Enter your Name: ")
#     exp = input("How much Experience do you have : ")
#     company = input("In which company do you have working on: ")
#     pro  = Programmer(name,exp,company) 
#     pro.worker()

# Problem_2

# class Calculator:
#     @staticmethod
#     def getcal(n):
#         print(f"Square of {n}^2 is {n**2}.")
#         print(f"Cube of {n}^3 is {n**3}.")
#         print(f"Squareroot of {n}^1/2 is {n**1//2}.")
# cal = Calculator()
# cal.getcal(4)

# class calculator:
#     def __init__(self, n):  #constuctor auto run the code
#         self.n = n
#     def square(self):
#         print(f"Square of {self.n} is {self.n**2}")
#     def cube(self):
#         print(f"Cube of {self.n} is {self.n**3}")
#     def squareroot(self):
#         if self.n < 0:
#             print("No any Squareroot of Imaginary number. ")
#         else:
#             print(f"Squareroot of {self.n} is {self.n**1//2}")
#     @staticmethod
#     def greet():
#         print("Hello! and welcome to mini calculator.")
# cal = calculator(-4)
# cal.greet()
# cal.square()
# cal.cube()
# cal.squareroot()

'''
PascalCase:
StartEnd -->>> PascalCase

camelCase:
startEnd -->>> camelCase
'''

# class Object:
#     a = "Python"
# obj = Object()
# obj.a = 0
# Object.a = 'Program'
# print(obj.a)
# print(Object.a)

# class Python:
#     def get(hooker ,name): # So we can take any parameter instead of self.
#         # hooker = self
#         hooker.name = name
#         print(hooker.name)
# py = Python()
# py.get('noop')

