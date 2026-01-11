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