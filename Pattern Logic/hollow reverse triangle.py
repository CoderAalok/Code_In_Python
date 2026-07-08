def hollowReverseTrianlge(n):
    for i in range(n):
        # hollow reverse left half trianlge
        for j in range(n):
            if i == 0 or j == i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        
        # hollow reverse right half trianlge
        for j in range(1, n):
            if i == 0 or j+i == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
            
        print()

hollowReverseTrianlge(5)
