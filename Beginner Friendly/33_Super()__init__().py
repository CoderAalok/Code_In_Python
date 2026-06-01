# Use of super().__init__()
class Parent:
    name = "Python"
    def __init__(self):
        self.name = self.name
        print("This is a parent constructor!")
    

class Interpreter(Parent):
    def __init__(self):
        super().__init__()
        print(f"Learning Phase....{self.name}")

class GetResult(Interpreter):
    def __init__(self):
        super().__init__()
        print(f"Complete {self.name}")
        
        
# obj_ = Interpreter()
obj = GetResult()  #It linked all classes 



# class Manager:

#     def __init__(self):
        # self.company = "Google"
#         print("Upload your resume and after verifition you will hired!")

# class Candidate(Manager):
#     def __init__(self):
#         super().__init__()
#         print(f"Uploaded... on {self.company}")

# class Test(Candidate):

#     def getTest(self):
#         print("Solve this problem??")

# # obj = Test()
# obj = Candidate()
# # obj = Test()
# # obj.getTest()
