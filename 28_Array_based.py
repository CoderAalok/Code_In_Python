# for i in range(1,100,2):
#     print(i)
# li1 = [-8,3,2,-3,-1,0,5]
# li2 = [i for i in li1 if i<=0]
# li2.sort()
# print(li2)

# pos = [i for i in range(-4,21) if i>=0]
# print(pos)
# def positive(start,end):
#     pos = [i for i in range(start,end) if i<0]
#     return pos
# print(positive(-10,10))
    

# li = [1,1,2,3,4,3,5,6,4,[],6,[],7,7,4 ]
# result = [i  for i in li if i != []]
# print(result)
# for i in li:
#     if i != []:
#         print(i,end=' ')
# for i in set(li):
#     print(i,end=' ')
# li = [12,3,44,55,2,1,1,1,2,3,4,3,66,3,32]
# # remove = [li[0],li[4],li[3]]
# # result = [i for i in li if i not in remove]
# # print(result)
# # li_new = li.copy()
# # print(li_new)
# print(li.count(3)) # also  can use to count character

# li = [12,3,(),2,1,1,1,3,(),66,3,32]
# re = [i for i in li if i != ()]
# print(re)

# li = [12,3,44,55,2,1,1,1,2,3,4,3,66,3,32]
# q = list(set(li))
# result = []

# print(result)

# li = [1,2,3,4]
# re = []
# sum_li = 0
# for i in li:
#     sum_li += i
#     re.append(sum_li)
# print(re)


#Sum of number digits in List
# arr = [123,456,789]
# val = []
# for i in arr:
#     total = 0
#     while i > 0:
#         total += i%10
#         i = i//10
#     val.append(total)
# print(val)
 

#Break a list into chunks of size N

# def chunks(li,N):
#     chunk_li = []
#     for i in range(0,len(li), N):
#         re = li[i:i+N]
#         chunk_li.append(re)
#     return chunk_li
           
# li = [12,3,44,55,2,1,1,1,2,3,4,3,66,3,32]
# N = 5
# print(chunks(li,N))

#Sort the values of first list using second list

# li1 = [2,4,3,6,5,7]
# li2 = ['a','s','d','f','c']
# val = [ i for (_,i) in sorted(zip(li2,li1))]  # by li2 sorting in li1
# print(val)



#TO finding the duplicate number...
# from collections import Counter
# li = [12,3,44,55,2,1,1,1,2,3,4,3,66,3,32]
# # n : m , where n is a number and m is that number how many times repeats
# count = Counter(li)
# #Too longer method 
# # count = {}
# # for i in li:
# #     if  i not in count:
# #         count[i] = 1
# #     else:
# #          count[i] += 1
# duplicate = [key for key, val in count.items() if val > 1]
# duplicate.sort()
# print(f"Here the duplicate numbers : {duplicate}")

# def duplicate(li):
#     count = {}
#     for key in li:
#         if key not in count:
#             count[key] = 1
#         else:
#             count[key] += 1
#     dup = [key for key , val in count.items() if val > 1]
#     return dup #count (repeated number with there value)
# li = [2,3,4,2,1,2,4,2,4,5,5,6,4,6,4,6,7,3]
# print(f"Here duplicate numbers are : {duplicate(li)}")

# li = ['dynamic programming', 'synchrogonized', 'brute force']
# for i, key in enumerate(li):
#     # key.title()  # this method can capitalized/ make upper case first character and remains character lower case.
#     print(key.title())

#Ascending order Unicode lexicographic order (same as Python’s built-in according to unicode
# li = ['dynamic programming', 'synchrogonized','thread', 'brute force']
# for _ in range(len(li)):
#     for i in range(1,len(li)):
#         if li[i-1] > li[i]:
#             li[i-1] , li[i] = li[i] , li[i-1]
# print(li)
# print(sorted(li))
# print('python' >'brute force') # according to unicode 

#prime numbers

# prime = []
# for i in range(100):  # O(n)
#     count = 0
#     for j in range(1,100): # O(n)
#         if i % j == 0 and i != 0 and i != 1:
#             count += 1
#     if count == 2:
#         prime.append(i)
# print(f"The prime numbers are {prime}")   # Net time complxity O(n^2) , not work for larger value...


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

#Python Vertical concatenation in matrix

# matrix = [['Be', 'from'], ['aware','uselesspeople'],['so be smart','be humble']]
# result = [[matrix[r][c] for r in range(len(matrix))] for c in range(len(matrix[0]))]
# print(result)
# final_count = []
# for i in result:
#     count = ' '
#     for j in i:
#         count += j
#     final_count.append(list((count).split()))
# print(final_count)

# matrix = [['Be', 'from'], ['aware','useless people'],['','so be smart']]
# val = [''.join(i) for i in zip(*matrix)]
# print(val)
# result = [[matrix[r][c] for r in range(len(matrix)) if c < len(matrix)] for c in range(len(matrix[0]))]
# re = []
# for i in range(len(result)):
#     concatenate = (''.join(result[i]))
#     re.append(concatenate)
# print(re)
#Whether the string is palindrome or not

# p = 'wow'
# q = p[::-1]
# if p == q:
#     print(f'Yes! {q} this is palindrome .')
# else:
#     print(f'No! {q} this is not palindome .')