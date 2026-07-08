def kPattern(n):
    for i in range(1, n):
        for _ in range(n-i):
            print("* ", end="")
        print()
    
    for j in range(1, n):
        for _ in range(j):
            print("* ", end="")
        print()

kPattern(5)

"""
Output:
* * * * 
* * * 
* * 
* 
* 
* * 
* * * 
* * * * 
"""