def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]*(i+1) # stats and ends with 1
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]  # sum two numbers directly above it
        triangle.append(row)

    # align at centre
    width = len(' '.join(map(str, triangle[-1])))
    for row in triangle:
        line = ' '.join(map(str, row))
        print(line.center(width))

pascal_triangle(6)

"""
Pascal's Triangle: each row starts and ends with 1 and inner numbers is equals to sum of two numbers directly above it.
Symmetric pattern (forward and backward same)
"""
# Output:
"""
      1      
     1 1     
    1 2 1    
   1 3 3 1   
  1 4 6 4 1  
1 5 10 10 5 1

"""