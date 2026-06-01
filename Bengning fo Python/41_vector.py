
# N-Dimension Vector
import numpy as np
class Vector:
    def __init__(self,vec1,pi=0.5):
        self.vec1 = vec1  #nD( n-Dimension of a vector)
        self.pi = pi

    def __check(self,vec2):
        if len(self.vec1) != len(vec2.vec1):
            raise ValueError("Vector dimension not equal!")
    
    
    def __format(self,sign):
        format = []
        for i,v in enumerate(sign):
            if v > 0:
                format.append(f"+ {v}k{i}")
            elif v < 0:
                format.append(f"- {abs(v)}k{i}")
            else:
                format.append(f"{v}k{i}")
            
        if format:
            
            format_result = " ".join(format)
            if format_result.startswith("+ "):
                return format_result[2:]
            return format_result
        
        return None
                
                
    def __add__(self,vec2):
        self.__check(vec2)
        add = [i+j for i,j in zip(self.vec1,vec2.vec1)]
        return  self.__format(add)
    
    def __sub__(self,vec2):
        self.__check(vec2)
        sub = [i-j for i,j in zip(self.vec1,vec2.vec1)]
        return  self.__format(sub)


    
    def __mul__(self,vec2):
        self.__check(vec2)
        dot_Product = sum([i*j for i,j in zip(self.vec1,vec2.vec1)])
        return (dot_Product,self.__magnitude(vec2))
    
    # Calculate magnitude of vectors(dot product)
    def __magnitude(self,vec2):
        magnitude_vec1 = (sum([i**2 for i in self.vec1]))**0.5
        magnitude_vec2 = (sum([i**2 for i in vec2.vec1]))**0.5
        
        magnitude = (magnitude_vec1*magnitude_vec2)*np.cos(self.pi)
        return round(magnitude,2)
    

if __name__ == "__main__":  # Using this to make this file name Vector ->> __main__
    a = (2,3,-4,3,-1)
    b = (2,-9,0,1,-5)

    v1 = Vector(a)
    v2 = Vector(b)
    
    print(f"Addition :   {(v1+v2)}")
    print(f"Subtration : {(v1-v2)}")
    
    prod,mag = v1*v2
    print(f"DotProduct : {prod}")
    print(f"Magnitude:   {abs(mag)}rad")
