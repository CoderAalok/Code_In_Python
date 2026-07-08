def reverseTrianlge(n):
    for i in range(n):
        for _ in range(i):
            print(" ", end=" ")
        for _ in range(n-i):
            print("*", end="   ")
        
        print()

reverseTrianlge(5)


# Output:
"""
*   *   *   *   *   
  *   *   *   *   
    *   *   *   
      *   *   
        *   

"""