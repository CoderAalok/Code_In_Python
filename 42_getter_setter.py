# This example hits the concept of Encapsulation 

class Teacher:
    def __init__(self,name,exp,taught):
        self._Name = name
        self._Exprience = exp
        self._Taught = taught

    @property
    def get_teacher(self):
        return self._Name
    
    @get_teacher.setter
    def get_teacher(self,value):
        self._Name = value
        return self._Name
    
    @property
    def get_exp(self):
        return self._Exprience,self._Taught
    
    @get_exp.setter
    def get_exp(self,exp):
        if exp > '1-years':
            self._Exprience = exp
            return self._Exprience
        else:
            raise ValueError("Experience atleast 2-years")
        
        
    
    
std = Teacher('Gamma','2-years','Mathematices') 
print(f"{std._Name}\n{std._Exprience}\n{std._Taught}\n") 

std.get_teacher,std.get_exp = 'Ram','5-years'
print(std.get_teacher)
print('\n'.join(std.get_exp))


