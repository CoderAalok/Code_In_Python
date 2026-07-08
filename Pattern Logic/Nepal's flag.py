def flag(n):
    for i in range(1, n):
        # Top right half pyramid
        for _ in range(i):
            print("*", end=" ")
        print()
    
    # Bottom right half pyramid
    for j in range(1, n):
        for _ in range(j):
            print("*", end=" ")
        print()
    
flag(5)


"""
Output:
* 
* * 
* * * 
* * * * 
* 
* * 
* * * 
* * * * 
"""
