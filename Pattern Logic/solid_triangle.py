def solidTriangle(n):
    for i in range(n):
        # step 1: Empty vertical right-angle triangle
        for j in range(n-i):
            print(" ", end=" ")
        
        # step 2: half right triangle
        for _ in range(i+1):
            print("*", end=" ")
        
        # step 3: half left triangle
        for _ in range(i):
            print("*", end=" ")
        
        # new line
        print()

solidTriangle(5)


"""
Output:
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * *
"""

# Alternative way
def solid_Triangle(n):
    for i in range(n):
        for _ in range(n):
            print(" ", end="")
        
        for _ in range(i): 
            print("*", end=" ") # just stretches left half pyramid
        
        print()

solidTriangle(5)


"""
Output:
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 

"""