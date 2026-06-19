def changing_pyramid(n):
    prev = 0
    for i in range(1, n+1):
        for _ in range(i):
            prev += 1
            print(f"{prev}", end=" ")
        
        print()

changing_pyramid(4)

"""
Output:
1
2 3
4 5 6
7 8 9 10

"""