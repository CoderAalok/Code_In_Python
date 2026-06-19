def Square(n):
    for i in range(n):
        for j in range(n):
            print("*", end="  ")
        print()
Square(6)

"""
Output:
*  *  *  *  *  *  
*  *  *  *  *  *  
*  *  *  *  *  *  
*  *  *  *  *  *  
*  *  *  *  *  *  
*  *  *  *  *  *
"""


# Similarly it's Hollow square
def hollowSquare(n):
    for i in range(n):
        for j in range(n):
            print(" ", end="")
            
            if i == 0 or j == 0 or j == n-1 or i == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        
        print()

hollowSquare(6)


"""
i == 0 -> first horizontal line only
j == 0 -> first vertical line only
j == n-1 -> last vertical line only
i == n-1 -> base or bottom line only
"""

"""
output:

*  *  *  *  *  * 
*              * 
*              * 
*              * 
*              * 
*  *  *  *  *  * 

"""