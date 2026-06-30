def rightPascalTriangle(n):
    for i in range(1, n):
        for _ in range(i):
            print("*", end="  ")
        print()
    
    for j in range(n):
        for _ in range(n-j):
            print("*", end="  ")
        print()

rightPascalTriangle(5)


"""
Output:
*  
*  *  
*  *  *  
*  *  *  *  
*  *  *  *  *  
*  *  *  *  
*  *  *  
*  *  
*  

"""