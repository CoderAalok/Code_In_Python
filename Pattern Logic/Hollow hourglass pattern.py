def hourglass(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == j or i + j == n-1 or i == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

hourglass(5)

"""
i == 0 -> first horizontal line
i == j -> left diagonal
i + j = n-1 - > right diagonal
i == n-1 -> last horizontal line

"""

# Output:
"""
* * * * * 
  *   *   
    *     
  *   *   
* * * * * 
"""