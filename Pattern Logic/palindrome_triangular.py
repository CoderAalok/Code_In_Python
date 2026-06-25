# First Logic
def palindromeTriangle(n):
    for i in range(n):
        # Step 1: Emtpy reversed right half pyramid
        for _ in range(n-i):
            print(" ", end=" ")
        
        # Step 2: Left half pyramid
        for j in range(i):
            print(i-j, end=" ")
        
        # Step 3: Right half pyramid
        for k in range(2, i+1):
            print(k, end=" ")
        
        # new line
        print()
        
palindromeTriangle(5)

# Second Logic (same output but not clarity)
def palindrome_triangle(n):
    for i in range(n):
        for _ in range(n-i):
            print(" ", end="")
            
        for j in range(i, 0, -1):
            print(j, end="")
        
        for k in range(2, i+1):
            print(k, end="")
            
        print()
        
        
palindrome_triangle(5)

"""
Step 2 -> start from i = 1,  inner loop j -> (0) => 1
                i = 2, j -> (0,1) => 2 1
                i = 3, j -> (0,1,2)  => 3 2 1
                i = 4, j -> (0,1,2,3) => 4 3 2 1

                
Step 3 -> start from i = 2+1, inner loop j -> (2)  => 2
                    i = 3+1, inner loop j -> (2,3)  => 2 3
                    i = 4+1, inner loop j -> (2,3,4) => 2 3 4
"""

"""
Output:

      1
    2 1 2
  3 2 1 2 3
4 3 2 1 2 3 4

"""