#Question_1

# class Car:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def get_brand_model_year(self):
#         print("____Here the Cars details____")
#         print("-------------------------")
#         print(f" Brand: {self.brand}")
#         print(f" Model: {self.model}")
#         print(f" Year: {self.year}")
#         print("-------------------------")
# c1 = Car("Roll's Royce","Phantom","2025")
# c2 = Car("Roll's Royce", "Cullinan","2024")
# c1.get_brand_model_year()
# print("-------------------------")
# c2.get_brand_model_year()
# print("-------------------------")

#Question_2

# class Student:
#     def __init__(self,students,subject,Mark):
#         self.students = students
#         self.sub = subject
#         self.mark= Mark
      
#     def get_student(self):
#         print(f"Name: {self.students}")
#         print("------------------------")
#     def get_marks(self):
#            for i, j in enumerate(self.mark):
#             print(f"Subject-{i+1}, Mark: {j}")
#             print("------------------------")

#     def get_average(self):
#        avg = 0
#        for a in self.mark:
#            avg += a
#        avg /= self.sub
#        return avg

# print("__Result__Published__")
# name = input("Enter your name: ")
# subject = int(input("How many subject do you have? >>> "))
# mark = []
# for i in range(1,subject+1):
#     marks = (int(input(f"Enter your Subject-{i} mark: ")))
#     mark.append(marks)

# std = Student(name,subject, mark)
# std.get_student()
# std.get_marks()
# print(f"The average of all {subject} subject is {std.get_average()}")
# print("------------------------")

# Question-3

# class Rectangle:
#     def __init__(self, length, breadth):  # constructor
#         self.l = length
#         self.b = breadth
#     def get_area(self):
#         area = self.l * self.b
#         print(f"The area of rectangle is {area}")

#     def get_perimeter(self):
#         perimeter  = 2*(self.l * self.b)
#         print(f"The perimeter of rectangle is {perimeter}")
# rec = Rectangle(12, 34)
# rec.get_area()
# rec.get_perimeter()


# Question-4
# class Dog:
#     def __init__(self,li_dogs,dic_breed):   #breed means varity of animal
#         self.name = li_dogs
#         self.breed = dic_breed

#     def get_name(self):
#         for i in self.name:
#             print(f">> {i}: {self.breed[i]}\n")
#     def bark(self):
#         print("\t\t\t Woof!")

# li_dogs = ["Labrador Retriever","German Shepherd","Bulldog"]
# dic_breed = {"Labrador Retriever":"friendly and loyal" ,
#              "German Shepherd":"Intelligent, used in police work",
#             "Bulldog":"Muscular, short-nosed face"
#             }
# animal= Dog(li_dogs,dic_breed)
# animal.get_name()
# animal.bark()


# Question-5

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