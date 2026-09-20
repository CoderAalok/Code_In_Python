def tree(n: int):
    for i in range(1, n-1):
        print(" "*(n-i) + "^ "*i)
        
    for i in range(1, n):
        print(" "*(n-i) + "^ "*(i))

    for i in range(1, n+1):
        print(" "*(n-i) + "^ "*i)

    for _ in range(n-1):
        print(" "*(n-3) + "*"*(n-2))

tree(5)