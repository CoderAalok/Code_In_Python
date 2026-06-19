def numberTriangle(n):
    for i in range(n):
        # Empty reverse right pyramid
        for _ in range(n-i):
            print(" ", end="")
        
        # left half pyramid just stretches
        for _ in range(i):
            print(f"{i}", end=" ")  # stretches (end=" ")
        
        # new line
        print()

numberTriangle(5)


"""
Output:
 
   1 
  2 2 
 3 3 3 
4 4 4 4 

"""