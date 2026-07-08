def mirrorImage(n):
    for i in range(1, n):
        # Top numeric trianlge
        for _ in range(i):
            print(" ", end="")
        
        for j in range(n-i):
            print((i+j), end=" ")
            
        print()
        
    # Bottom  numeric triangle
    for i in range(2, n):
        for _ in range(n-i):
            print(" ", end="")
        
        for j in range(i, 0, -1):
            print(n-j, end=" ")
        
        print()
    
mirrorImage(5)


"""
Output:

 1 2 3 4 
  2 3 4 
   3 4 
    4 
   3 4 
  2 3 4 
 1 2 3 4 
 
"""