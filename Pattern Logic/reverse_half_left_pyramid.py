def reverse_left_pyramid(n):
    for i in range(n):
        for _ in range(i):
            print(" ", end="")
        
        for _ in range(n-i):
            print("*", end="")
        
        print()
    
reverse_left_pyramid(6)

"""
Output:

******
 *****
  ****
   ***
    **
     *
"""

# Similarly it's hollow
def hollow_reverse_left_pyramid(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == j or j == n-1:
                print("*", end="")
            else:
                print(" ", end="")
        
        print()

hollow_reverse_left_pyramid(6)


"""
i == 0 -> first row only
i == j -> diagonal
j == n-1 -> last column only
"""

"""
Output:
******
 *   *
  *  *
   * *
    **
     *

"""