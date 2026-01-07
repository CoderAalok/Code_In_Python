class Operator:

    def __init__(self,num1,num2,s):
        self.num1 = num1
        self.num2 = num2
        self.s = s

    def __add__(self,num2):
        return self.num1+num2.num1 + self.num2+num2.num2, self.num2+self.num1   
    
    def __truediv__(self,num2):
        return (self.num1+num2.num1) / (self.num2+num2.num2)  
    
    def __str__(self):
        return self.s[:6]

class String(Operator):  
    
    def __init__(self,strr):
        self.s = strr
        
    def __str__(self):
        return f"{self.s}"
        
    def __len__(self):
        return len(self.s)
    
a = Operator(12,0,'Abstraction') 
b = Operator(3,4,'Proposal')
print(a+b)

print(a/b)
print(b)

obj = String("Encapsulation")

print(obj)

print(len(obj))
