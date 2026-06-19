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
        for _ in range(n-i):
            print(" ", end="")
        
        for _ in range(i):
            print("*", end=" ")

        print()

solid_Triangle(5)

"""
Output:
    * 
   * * 
  * * * 
 * * * * 

"""

# Similarly its Hollow trianlge
def hollow_triangle(n):
    for i in range(n):
        
        for j in range(n):
            if i+j == n-1 or i == n-1:
                print("*", end="")
            else:
                print(" ", end="")

        for k in range(1, n):
            if i == k or i == n-1:
                print("*", end="")
            else:
                print(" ", end="")

        print()
    
hollow_triangle(5)


"Same logic as left and right half hollow pyramid just ignore middle"

"""
Output:
with stretches (end=" ")
        *         
      *   *       
    *       *     
  *           *   
* * * * * * * * * 

without stretches (end="")
    *    
   * *   
  *   *  
 *     * 
*********

"""