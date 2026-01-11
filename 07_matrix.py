# # Identical Matrix without function
# row = int(input("Enter number of rows : "))
# col = int(input("Enter numner of columns : "))
# matrix  = []
# for i in range(row):
#     matrix1 = []
#     for j in range(col):
#         user = int(input(f" {(i+1)} Row and {(j+1)} Column = "))
#         matrix1.append(user)
#     matrix.append(matrix1)
# length_matrix = len(matrix)
            
# print(f"The matrix of {row} row and {col} column is ")
# for k in matrix:
#     for i in k:
#         print(i,end="  ")
#     print()
# count = 0
# # for r in range(length_matrix):  #This approach is not relevant 
# #     for c in range(length_matrix):
# #         if r == c and matrix[r][c] == 1:  
# #             count +=1
            
# # if count == 2 or count == 3:
# #     print("It is an Identity matrix")
# # else:
# #     print("Non Identity matrix ")
    
    
def identity_matrix(matrix):
    length_matrix = len(matrix)
    for r in range(length_matrix):
        for c in range(length_matrix):
            if  r == c and matrix[r][c] > 1:
                return False 
            if r != c and matrix[r][c] != 0:
                return False
    return True 
row = int(input("Enter number of rows : "))
col = int(input("Enter numner of columns : "))
matrix  = []
if not  row == col:
    print("Row and Column must be equal")
else:
    for i in range(row):
       mat = []
       for j in range(col):
          user = int(input(f" {(i+1)} row and {j+1} column"))
          mat.append(user)
       matrix.append(mat)
    print(identity_matrix(matrix))

            
            
    # if row == col:
    #     continue
    # else:
    #     print("Row and Column are not equivalent.")
        





#Addind  and subtracting two matries 

# m1 = [[1,2] , [3,4]]
# m2 = [[5,6] , [7,8]]
# add_m = []
# sub_m = []
# for i in range(len(m1)):
#     m3 = []
#     m4 = []
#     for j in range(len(m2)):
#         sum1 = m1[i][j] + m2[i][j]
#         sub = m1[i][j] - m2[i][j]   
#         m3.append(sum1)
#         m4.append(sub)
#     add_m.append(m3)
#     sub_m.append(m4)
# print(f"The adding of two matrices {m1} and {m2} : ")
# for k in add_m:
#     print("\t",k,end =' ')
#     print()
    
# print(f"The subracting of two matrices {m1} and {m2} : ")
# for i in sub_m:
#     print("\t", i , end=' ')
#     print()


#Multiplication of two matrices only valid for 2*2 matrix

# m1 = [[1,2] , [3,4]]
# m2 = [[5,6] , [7,8]]
# multi_m = [] # Calculated elements are  inside the list 
# for r in range(len(m1)):
#     count = [] # count 0th and 3rd indices value
#     for c in range(len(m2)):
#         k1 = m1[r][c]*m2[c][r]
#         count.append(k1)
#     multi_m.append(sum(count))
# for i in range(len(m1)):
#     count_1 = [] # Count 1st and 2nd indices value 
#     for j in range(len(m2)):
#         k2 = m1[i][j] * m2[j][1-i]
#         count_1.append(k2)
#     multi_m.append(sum(count_1))
# # Swipping 1st to 2nd , 2nd to 3rd and 3rd to 1st (make perfect arrangement format) 
# M = multi_m[1]
# multi_m[1] = multi_m[2]
# multi_m[2] = multi_m[3]
# multi_m[3] = M

# new_m = [] # Re-arranged and make prefect matrix format
# for k in range(1):
#     count_ = [] # 0th and 1st
#     count_0 = [] # 2nd and 3rd
#     for j in range(2):
#         count_.append(multi_m[j])
#     new_m.append(count_)
#     for i in range(2,4):
#         count_0.append(multi_m[i])
#     new_m.append(count_0)
# print("The multiplication of two matrices is  ")
# for i in (new_m):
#     print(i,end=' ')
#     print() # new_line
    
# This method valid for any type of matrix

# def matrix_multiplication(m1,m2):
#     matrix = [] # Matrix Format
#     for r in range(len(m1)): # Number of rows of matrix_1
#         arg = []
#         for c in range(len(m2[0])):  # Number of column of matrix_2
#             sum_matrix = 0
#             for k in range(len(m2)): # Number of columns of matrix_1 and rows of matrix_2
#                 sum_matrix += m1[r][k] * m2[k][c]
#             arg.append(sum_matrix)
#         matrix.append(arg)
#     return matrix
# m1 = [[1,2,3] , 
#     [3,4,2]]

# m2 = [[5,6,3] ,
#     [7,8,2]]
# matrix = matrix_multiplication(m1,m2)
# print("The multiplication of two matrices is: ")
# for i in matrix :
#     print(i,end='')
#     print()

#Simplest method using list comprehensive.....
# def matrix_multiplication(m1,m2):
#     '''Working Process: Initillization from outer loop <'for r'> 
#       and enter in inner loop <for c> and after then go to 
#       inner_most loop <for k> loop. And the process until run for complition of 
#       <for k and c loops> '''
#     ''' summing process : during the running <for k _loop>, until sum
#      complition of <for k _loop>'''
#     matrix = [[sum(m1[r][k] * m2[k][c] for k in range(len(m2))) for c in range(len(m2[0]))] for r in range(len(m1))]
#     return matrix
# m1 = [[1,2,3] , 
#     [3,4,2]]

# m2 = [[5,6,3] ,
#     [7,8,2]]
# matrix = matrix_multiplication(m1,m2)
# print("The multiplication of two matrices is: ")
# for i in matrix :
#     print(i,end='')
#     print()


# #Product of inner matrix elements
# m1 = [[1,2,3] , 
#     [3,4,2]]
# m2 = [[5,6,3] ,
#     [7,8,2]]

# result = 1 
# val = [j for i in m1 for j in i]
# for k in val:
#     result *= k
# print(result)

# # sum of two matrices and product them
# result = 0
# val_1 = [sum(j for i in m1 for j in i)]
# val_2 = [sum(j for i in m2 for j in i)]
# result = sum(val_1)* sum(val_2)
# print(result)


#Transpone of matrix

# matrix = [[1,2] ,
#          [3,4] , 
#          [5,6]]
#[[1,3,5] , [2,4,6]]
# transpose = [i for i in zip(*matrix)] # This zip(*matrix) take every elements which lies on first index
# print(transpose)
# transpose = [[matrix[r][c] for r in range(len(matrix))] for c in range(len(matrix[0]))]
# for i in transpose:
#     print(i,end=' ')
#     print()

# result_odd = [j for i in matrix for j in i if j % 2 != 0 ]
# transpose.append(result_odd)
# result_even = [j for i in matrix for j in i if j % 2 == 0 ] 
# transpose.append(result_even)
# print(transpose)


# import bisect
# a = [3,4,5,5,3,1,7]
# # a.sort()
# b = []
# for i in a:
#     q = bisect.bisect(b,i) #bisect() module , it finds location of an elements where does it inserted to keep it sorted.
    
#     b.append(q)
# b.sort()
# print(b)

# Matrix creation of n*n
#Approach of n*n matrix
# def matrix(size):
#     matrix_n = []
#     for r in range(size):
#         count = []
#         for c in range(size):
#             val_ = int(input(f" Row: {r+1} * Column: {c+1} = "))
#             count.append(val_)
#         matrix_n.append(count)
#     return matrix_n
# size = 2
# print(f"The matrix of {size}*{size} is ")
# for i in matrix(size):
#     print(i)
    
#Alternative method
# n = 4
# matrix = [[c for c in range(n)] for r in range(n)]
# for i in matrix :
#     print(i)


#Get Kth column of matrix
# matrix = [[1,3,4],
#           [2,3,5],
#           [3,4,5]]
# k = 0
# result = [[matrix[r][k] for r in range(len(matrix))]]
# print(f"The given matrix: {matrix} and ")
# print()
# print(f"The given matrix {k+1} column: ")
# for i in result:
#     print("\t",i)+
