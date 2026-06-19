def reverse_increasing(n):
    for i in range(n):
        for j in range(n-i):
            print(f"{j+1}", end=" ")
        
        print()

reverse_increasing(5)

"""
Output:

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

"""