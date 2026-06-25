def diamondPattern(n):
    # First part: Triangle
    for i in range(n):
        # step 1: Emtpy reversed right half pyramid
        for _ in range(n-i):
            print(" ", end="")
        
        # step 2: Left half pyramid
        for _ in range(i):
            print("*", end=" ")
        
        print()
    
    # Second part: Reversed Triangle
    # step 3: Empty right half pyramid
    for j in range(n):
        for _ in range(j):
            print(" ", end="")
    
        # step 4: Reversed left half pyramid
        for _ in range(n-j):
            print("*", end=" ")
    
        print()
    
diamondPattern(4)

"""
Output:

   * 
  * * 
 * * * 
* * * * 
 * * * 
  * * 
   * 
   
"""


# Similarly it's hollow
# def hollowDiamondPattern(n):
#     # First Part: Hat
#     for i in range(n):
#         # first line
#         for j in range(n):
#             if i+j == n-1:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         # second line
#         for k in range(1, n):
#             if i == k:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()

#     # Second Part: Reversed Hat
#     for j in range(1, n):
#         for k in range(n):
#             if k == j:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
        
#         for m in range(1, n):
#             if j+m == n-1:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
                
#         print()
    
# hollowDiamondPattern(4)



"""

Output:

   *   
  * *  
 *   * 
*     *
 *   * 
  * *  
   *   
   
"""

# compressed logic
def hollowDiamondPattern(n):
    for i in range(n):
        # First part: Top hat
        for j in range(2*n-1):
            if j+i == n-1 or j-i == n-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
        
    # Second part: Reversed hat
    for i in range(n-2, -1, -1):
        for k in range(2*n-1):
            if k+i == n-1 or k-i == n-1:
                print("*", end="")
            else:
                print(" ", end="")
        
        print()

hollowDiamondPattern(4)