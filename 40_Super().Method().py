class Owner:
    
    def get_more(self):
        print("New features add to joining us....")
        li = list(range(0,10,2))
        print(li)

class Worker(Owner):
    
    def get_accept(self):
        super().get_more()
        print("We're try to do...")
        
obj = Worker()
obj.get_accept()







"""
add validation (e.g., age can’t be negative)

hide internal implementation

keep attribute syntax simple

avoid breaking code when logic changes
"""





# # class Workers:
# #     salary1 = 500
# #     salary2 = 1000
    
# class Increment(Workers):
    
#     # def get_salary(self,salary):
#     #     self.__class__.salary2 = salary
#     #     print(self.__class__.salary2)
    
#     @classmethod
#     def get_salary(cls,salary):
#         cls.salary1 = salary
#         print(cls.salary1)
        
    
# obj = Increment()
# obj.get_salary(600)
# print(obj.salary1)
