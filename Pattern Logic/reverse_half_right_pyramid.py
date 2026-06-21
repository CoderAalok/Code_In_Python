def reverse_right_pyramid(n):
    for i in range(n):
        for j in range(n-i):
            print("*", end="")
        print()

reverse_right_pyramid(6)

"""
Output:

******
*****
****
***
**
*

"""


# Similarly, it's hollow
def hollow_reverse_right_pyramid(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i+j == n-1:
                print("*", end="")
            else:
                print(" ", end="")
        
        print()

hollow_reverse_right_pyramid(6)


"""
i == 0 -> first row only
j == 0 -> first column only
i+j == n-1 -> diagonal
"""

"""
Output:

******
*   *
*  *
* *
**
*     

"""