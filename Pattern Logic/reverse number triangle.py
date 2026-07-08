def reverseNumberTriangle(n):
    for i in range(1, n):
        for _ in range(i):
            print(" ", end="")
            
        for j in range(n-i):
            print((i+j), end=" ")
        print()
    
reverseNumberTriangle(5)

"""
Output:
 1 2 3 4 
  2 3 4 
   3 4 
    4 
"""

