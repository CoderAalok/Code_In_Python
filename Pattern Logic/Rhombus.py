def rhombusPattern(n):
    for i in range(n):
        for _ in range(i):
            print(" ", end="")
        
        for j in range(n-1):
            print("*", end=" ")
        
        print()
        
rhombusPattern(5)

"""
Output:

* * * *
 * * * *
  * * * *
   * * * * 
    * * * *

"""