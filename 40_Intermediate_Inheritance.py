# Practice-I
class Teacher:

    def types_Teacher(self):
        print("----Here below types of teacher based on subject----")
        
        print("Teacher_1: Mathematices")
        print("Teacher_2: Physics")
        print("Teacher_3: Chemistry")

class Author:
    def book_authors(self):
        print("Authored by (Author_1): Mathematices")
        print("Authored by (Author_2): Physics")
        print("Authored by (Author_3): Chemistry")

class Personality(Teacher,Author):
    def get_detail_teacher_authors(self):
        super().types_Teacher()
        super().book_authors()

p = Personality()
p.get_detail_teacher_authors()

# ----------------------------------------------------------------------------------------- 

# Practice-II
class Shape:
    def area_shape(self):
        pass
    
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b  
  
    def get_area(self):
        return self.l*self.b

class Triangle(Shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b       

    def get_area(self):
        return 0.5*(self.l*self.b)

rec = Rectangle(4,5)
tri = Triangle(8,70)

print(f"Area of rectangle: {rec.get_area()}")
print(f"Area of triangle: {tri.get_area()}")


# ----------------------------------------------------------------------------------------

