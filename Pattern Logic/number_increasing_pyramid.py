def increasingPyramid(n):
    for i in range(1, n):
        for j in range(i):
            print(f"{j+1}", end=" ")
            
        print()
        
increasingPyramid(5)

"""
Output:
1
1 2
1 2 3
1 2 3 4
"""