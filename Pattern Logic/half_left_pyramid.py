def halfLeftPyramid(n):
    for i in range(n):
        for _ in range(n-i):
            print(" ", end="")
        
        for _ in range(i):            
            print("*", end="")
        print()
        

halfLeftPyramid(5)

"""
Output:
     
    *
   **
  ***
 ****

"""

# Similar it's Hollow 
def hollowhalfLeftPyramid(n):
    for i in range(n):
        for _ in range(n):
            print(" ", end="")
        
        for j in range(n):
            print(" ", end="")
            
            if j == n-1 or n-1 == i+j or (n-1) == i:
                print("*", end="")
            else:
                print(" ", end="")
        
        print()

hollowhalfLeftPyramid(5)

"""
j == n-1 -> right vertical line
n-1 == i+j -> diagonal
n-1 == i -> base
"""

"""
Output:
              *
            * *
          *   *
        *     *
      * * * * *
"""