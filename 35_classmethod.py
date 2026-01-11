class Workers:
    salary = 500
    bonusPoint = 1000
    
    @classmethod
    def get_change(cls,val):
        cls.bonusPoint = val
        return cls.bonusPoint + cls.salary
w = Workers()
print(w.get_change(900))


# class Increment(Workers):
    
    # def get_salary(self,salary):
    #     self.__class__.salary2 = salary
    #     print(self.__class__.salary2)
    
    # @classmethod
    # def get_salary(cls,salary):
    #     cls.salary1 = salary
    #     return cls.salary1 + cls.bonusPoint
        


# obj = Increment()
# print(obj.get_salary(600))
# print(obj.salary1)

