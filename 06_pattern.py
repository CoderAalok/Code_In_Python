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
        
         