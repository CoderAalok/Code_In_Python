# import time
# class Client:
#     def get_Info(self,info):
#         self.info = info
#         return info

# #Here request come client to browser
# class Browser(Client):
#     def request_client(self):
#         keep = super().get_Info(info) 
#         print("Client request move to the server...")        

# #browser to server
# class Server(Browser):
#     def request_browser(self):
#         if hasattr(self,'info') and self.info.strip() != ""  :
#             return True
#         else:
#             return False

# info = input("🔎Search anything....")
# endUser = Client()
# endUser.get_Info(info)

# web = Browser()
# web.request_client()

# sys = Server()
# sys.get_Info(info)
# result = sys.request_browser()

# print("Verifying the request...")
# time.sleep(1)

# if result:
#     print(f"Request successfully processed!")
# else:
#     print("404:request fail...")


# class ChatGPT: #Base Class
#     version = 'GPT-5'
#     def getChat(self,name):
#         print(f"{self.version}Hi {name.title()}! What's on your mind today's?")

# class Programmer(ChatGPT): #Derived Class1
#     def getquestion(self):
#         print(">> Something new and updated technology!")

# class AnsGPT(Programmer): #Derived Class2
#     def getAnswer(self):
#         super().getChat('alpha')
#         print("""
# Here, today the techonology move on next level generative AI,\n
# AI and ML reaching top level which is 6G in upcoming generation
# """)

# # name = input("Name: ").strip()
# gpt = AnsGPT()
# # gpt.getChat(name)
# # gpt.getquestion()
# gpt.getAnswer()


# class Parent:
#     def method(self):
#         print("Decorator of Parent class")
# class Child(Parent):
#     def method(self):
#         print("Decorator of Child class")
# clss = Child()
# clss.method()   #Python always gives first priority derived class


# class Employee:
#     def get_income(self):
#         print("Just earning......")

# class Person(Employee):
#     def get_work(self):
#         print("Still work on...")
        
#     # def get_income(self):
#         # print("Just earning... and learning...")
# class Manager(Person):
#     def get_manage(self):
#         # super().get_income()
#         super().__init__(self,Employee)
#         print("Company holder...")
        
# # e = Employee()
# # e.get_income()

# # p = Person()
# # p.get_work()
# # p.get_income()

# m = Manager()
# m.get_manage()
# # m.get_income()
# m.get_work()

