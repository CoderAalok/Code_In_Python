# Practical Example: Multiple Inheritance
# (Using single derived class access both Base class methods)

# class Student1: #Base class
#     std1 = 'Jack'#Property
#     def result1(self):  #Method
#         print(f"{self.std1} fail in Mathematics\nonly 10 out of 100 scored!")

# class Student2:  #Base class
#     std2 = 'Mice'
#     def result2(self):
#         print(f"{self.std2} passed with good score in all subjects.")
# class Price:
#     def result3(self):
#         print("And also, Good scored obtained students must recived there own telent price!")

# class Teachers(Student1,Student2,Price):  #Derived class
#     def failure(self):
#         print("Teacher gives permission who fail!")


# result = Teachers()
# result.result1()
# result.result2()
# result.failure()
# result.result3()

class Demo:
    pass
obj = Demo()
obj.name = "Python" #instance attribute
print(obj.name)