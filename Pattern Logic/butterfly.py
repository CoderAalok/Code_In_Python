def butterflyStart(n):
    for i in range(1, n):
        for _ in range(i):
            print("*", end="  ")
        
        for _ in range(2*(n-i), 3, -1):
            print(" ", end="  ")
        
        for k in range(i):
            print("*", end="  ")
        
        print()
    
    for j in range(2, n):
        for _ in range(n-j):
            print("*", end="  ")
        
        for _ in range(2*j, 3, -1):
            print(" ", end="  ")
            
        for k in range(n-j):
            print("*", end="  ")
        
        print()

butterflyStart(5)
            
    
    
print()
    
def hollowButterflyStart(n):
    for i in range(n):
        for j in range(n):
            if j == 0 or j == i or j+i == n-1 or j == n-1:
                print("*", end="  ")
            else:
                print(" ", end="  ")
        print()

hollowButterflyStart(5)
"""
*           *  
*  *     *  *  
*     *     *  
*  *     *  *  
*           *  
"""