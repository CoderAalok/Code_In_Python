def halfRightPyramid(n):
    for i in range(n):
        print("*"*(i+1), end=" ")  #  end="" -> gap between starts
        print()
        
halfRightPyramid(6)

"""
Output:
*
**
***
****
*****
"""

# Similarly it's Hollow

def hollowHalfRightPyramid(n):
    for i in range(n):
        for j in range(n):
            print(" ", end="") 
            
            if j == 0 or i == j or (n-1) == i:
                print("*", end="")
            else:
                print(" ", end="")

        print()

hollowHalfRightPyramid(6)


"""
j == 0 -> left vertical line
i == j -> diagonal
n-1 == i -> base
"""

"""
Output:
*          
* *        
*   *      
*     *    
*       *  
* * * * * *
"""