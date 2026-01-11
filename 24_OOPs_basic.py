# # class Company:
# #     com1 = 'Youtube'
# #     print(com1)
# # con = Company()
# # con.com1 = 'Google'
# # print(con.com1)
    

# class Student:
#     _student_ = 'Good Student'
#     def std(self,name):
#        self.name = name
#         # def __init__(self , name): #__init__() is called a constructor.
#         #It's a special method that automatically run when we 
#         # create(initialize)an object from a class.

#method-1
# #creating new empty object
# # s1 = Student('jack')  # now s1 is empty and
# # s2 = Student('mock') # also s2

#method-2
# s1 = Student() # first go to class and 
# s1.std('Jack') # calling function
# s2 = Student() # second go to class and 
# s2.std('Nike') # calling function
# print(s1.name,'\n',s2.name)

# Class Attribute

# class Student:
#     info = "Good Morning, Dear student!"
#     #def __init__(self, name):
#     def std(self, name):
#         self.name = name  # self detect class variable which create new empty object
        
# s1 = Student()  #creates empty object of a class
# s1.std("World king The") #but s1 it knows it belongs to class and class call std() 
# s2 = Student()
# s2.std('GOD VISHNU')
# print(s1.name , s2.info)
# # s1 = Student("Yake")
# # s2 = Student("Jackie")
# # print(f" {s1.name} {s1.info}, {s2.name} {s2.info}")


# Instance Attribute 

# class Employee:
#     company = "Google"
#     package = 8000000
# call = Employee()
# print(call.company)
# call = Employee()
# call.company = "Microsoft"  # Class looks any instances outside of..........>>>
# #if yes then that object print else inside of class 
# print(call.company)
# #Like this >>>> there is no any instance of package out side of class so, still print inside created object
# print(call.package)



# class Click:
#     left_botton = False
#     if not left_botton:
#         print(None)
#     else:
#         print("Successfully, you enter Coding zone!")
# call = Click()
# # call.left_botton = False
# print(call.left_botton)
# class Bank_amount:
#     bank = "SBI"
#     def getincome(self ,money,rate):
#         print(f"Hi! current bank balance in your {self.bank} bank is {money} and increment with intrest {rate}.")
# call = Bank_amount()
# call.money = 1000000  # instance attribute
# call.getincome(call.money, "2%") # or Bank_amount.getincome(call)

#for doing this...>>>
#self variable automatically detect 'call'
#And then call variable use to prints both Instance and Class attributes
# Bank_amount.getincome(call , call.money,"2%") 

#Pass
# class game:
#     open = input("Tap to enter and open Dynamic Game: ")
#     fun = {1:'Cap', 2:'Mobile', 3:'Laptop'}
#     if open == ' ':
#         print(f"Let's play!")
#         print()
#         chose = int(input("Enter your desire Number: "))
#         if chose in [1,2,3]:
#             print(f"Congratulation! you select a {chose} Number and you will win {fun[chose]}. ")
#         else:
#             print("Try next time!")
# open = game()



#staticmethod

# class Manager:
#     company = 'Google'
#     def __init__(self):
#         print(f" Great! Opportunity for Security Management in {self.company}. \n fill your details and get this opportunity without delay.")
#     @staticmethod
#     def assist(name, address, Email):
#         print(f"Your Name: {name}")
#         print(f"Your Address: {address}")
#         print(f"Your E-mail: {Email}")
#     @staticmethod
#     def verify():
#         print("Thanks! for filling your details.\n You will get message after verification your details.")
# cal = Manager()
# # cal.greet()
# # cal.assist(200,100) # Assistain.assist(200,5000)
# a = input("Enter your Name: ")
# b = input("Enter your Address : ")
# c = input("Enter your E-mail: ")
# cal.assist(a,b,c)
# print()
# cal.verify()



