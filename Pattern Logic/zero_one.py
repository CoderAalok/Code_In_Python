def zeroOne(n):
    for i in range(n):
        for j in range(1, i):
            if (i+j) % 2 == 0:
                print(0, end=" ")
            else:
                print(1, end=" ")
        print()

zeroOne(6)


"""
Output:

1
0 1
1 0 1
0 1 0 1

"""