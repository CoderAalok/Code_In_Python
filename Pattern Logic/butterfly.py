def hollowButterflyStart(n):
    for i in range(n):
        for j in range(n):
            if j == 0 or j == i or j+i == n-1 or j == n-1:
                print("*", end="  ")
            else:
                print(" ", end="  ")
        print()

hollowButterflyStart(5)
