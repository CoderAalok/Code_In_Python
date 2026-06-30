def reverseHollowTriangle(n):
    for i in range(n):
        # Left half
        for j in range(n):
            if i == 0 or j == i:
                print("*", end="")
            else:
                print(" ", end="")
        
        # Right half
        for k in range(1, n):
            if i == 0 or k+i == n-1:
                print("*", end="")
            else:
                print(" ", end="")
          
        print()
        
reverseHollowTriangle(5)


"""
Output:

*********
 *     * 
  *   *  
   * *   
    *    
"""