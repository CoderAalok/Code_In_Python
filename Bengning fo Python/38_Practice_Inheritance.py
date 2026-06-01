# Practice: 1

# class C2dvec:
    
#     def __init__(self,i,j):
#         self.i = i
#         self.j = j
    
#     def __str__(self):
#         return f'{self.i}i+{self.j}j'
    
# class C3dvec(C2dvec):
    
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k = k
        
#     def __str__(self):
#         return f'{self.i}i+{self.j}j+{self.k}k'

# vec2D = C2dvec(1,9)
# print(f"{vec2D}")

# vec3D = C3dvec(3,6,4)
# print(f"{vec3D}")


#-------------------------------------------------------------------------

# Practice: 2
# class Animal:
    
#     def __init__(self,animals,pets):
#         self.animal = animals
#         self.pets = pets

#     def li_animal(self):
#         return self.animal
    
#     def li_pets(self):
#         return self.pets

# class Pets(Animal):
    
#     def animal_pets(self):
        
#         li_animal = super().li_animal()
#         li_pets = super().li_pets()
        
#         dict_animal = {}
#         for i in range(len(li_animal)):
#             dict_animal[li_animal[i]] = li_pets[i]

#         return dict_animal  
        

# class Dogs(Pets):
#     def bark(self):
#         print("The dogs everytime brak on the road side...")

# animals = ['Dogs','Cats',"Leopad",'Lion','Monkey']
# pets = ['Puppy','Ketty','Cub','LionCub','Infant']

# # obj_animal = Animal(animals,pets)

# obj_pets = Dogs(animals,pets)
# result = obj_pets.animal_pets()

# print(f"Here some domastic animal:")
# for k,v in result.items():
#     print(f"{k}:{v}")

# obj_pets.bark()

#-------------------------------------------------------------------------

# Practices: 3
# class Employee:
#     # Class attributes
#     name = "Worker"
#     salary = 500
#     increment = 2.5
    
#     @property #getter access and only read from a class
#     def salaryAfterIncrement(self):
#         return self.increment
    
#     # Modify using setter
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self,sal):
#         self.increment = sal/self.salary
#         return self.increment

# salary = int(input("Enter a new salary: ").strip())

# e = Employee()

# print(f"The increment of salary is {e.increment}%  before!")

# e.salaryAfterIncrement = salary
# print(f"And now after increment of salary is {e.salaryAfterIncrement}% ") 


#-------------------------------------------------------------------------

# Practice: 4
# Method: I
# class Complex:
    
#     def __init__(self,z):
#         self.z = z
    
#     def __add__(self,z1):
#         return self.z+z1.z
    
#     def __mul__(self,z1):
#         return self.z*z1.z

# z = complex(2,3) 
# z1 = complex(1,5)

# a = Complex(z)
# b = Complex(z1)

# print(a+b)
# print(a*b)

# Method: II
class Complex:
    
    def __init__(self,re,img):
        self.re = re
        self.img = img
    
    def __add__(self,r):
        
        real = self.re+r.re
        img = self.img+r.img
        
        if img<0:
            return f'{real}-{-img}i'
        else:
            return f'{real}+{img}i'
            
    def __mul__(self,r):
        
        mulreal = self.re*r.re - self.img*r.img
        mulimg = self.re*r.img + self.img*r.re
        
        if mulimg<0:
            return f'{mulreal}-{-mulimg}i'
        else:
            return f'{mulreal}+{mulimg}i'



a = Complex(1,9)
b = Complex(2,5)

print(a+b)
print(a*b)

#-------------------------------------------------------------------------
# Practice: 5

# class Vector:
    
#     def __init__(self,vecA):
#         self.vecA = vecA
        
#     def __add__(self,vecB):
        
#         if len(self.vecA) != len(vecB.vecA):
#             raise ValueError("Both vector must equal")
        
#         sumVec = [self.vecA[i]+vecB.vecA[i] for i in range(len(self.vecA))]
        
#         return tuple(sumVec)

#     def __mul__(self,vecB):
        
#         if len(self.vecA) != len(vecB.vecA):
#             raise ValueError("Both vector must equal")
        
#         dotprod = [self.vecA[i]*vecB.vecA[i] for i in range(len(self.vecA))]
        
#         return sum(dotprod)

#     def __len__(self):
#         return len(self.vecA)

# a = (2,3,1)
# b = (1,3,0)

# vec1 = Vector(a)
# vec2 = Vector(b)

# print(f"Add of two vector: {vec1+vec2}")
# print(f"Multiply of two vector: {vec1*vec2}")

# print(f"Dimension of vector'A': {len(vec1)}D ")

#-------------------------------------------------------------------------

#Practice: 6
# class Vector3D:
    
#     def __init__(self,i,j,k):
#         self.veci = i
#         self.vecj = j
#         self.veck = k

#     def __str__(self):
#         return f'{self.veci}i+{self.vecj}j+{self.veck}k'

# vec = Vector3D(2,4,0)
# print(vec)

#-------------------------------------------------------------------------



