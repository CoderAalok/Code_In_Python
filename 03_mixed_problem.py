<<<<<<< HEAD
# #Basic slicing
# #q = 'The most genuine programming language is Python'
# # print(q[:-4]) 

# #Extebded slicing
# # num  = '1 3 4 5 6 7 8 9'
# # print(len(num))
# # print(num[3::3])
# # print(num[-4::10])
# # print(num[7::-10])

# #Start , end , step
# # a = 'Retrieval Agument Generation'
# # print(a[:5:1])
# # print(a[:0:2])
# # #print(a[::0])#cannot have step as 0
# # print(a[3:6:9])

# #sclicing in a list
# # lst = [1,2,3,4,5,6,7,8,9]
# # print(lst[:8:3])

# str = 'My journey in my coding is clear'
# # q=str.replace('My','Explicitly')
# # l=len(q)
# # print(q , str[::-1])
# # upper =  str.upper()
# # lower = str.lower()
# # print(upper , lower)
# # print(str.center(100))
# # w = str.count('a')
# # if w == 1:
# #     print(f'There is {w} occurance of a')
# # else:
# #     print('none')
# print(str.isdigit())
# print(str.isalpha())
# print(str.strip())
# print(str.split())
# print(''.join(reversed(str)))

# print(list(str))
# print(tuple(str))
# print(set(str))


# li =  ['apple', 'dragon fruit' ]
# print(li.count('apple'))
# print(li.index('apple'))


#dictionary
# str = 'Database is a collection of interrelated data'
# dict = {}
# for i in str:
#     if i in dict:
#         dict[i] += 1
#     elif i == '':
#         continue
#     else:
#         dict[i] = 1
# print(dict)


# li = [1,2,[3,4],5,6,[7,8,9]]
# print(li[2][-1])
# tuple = (3,5,6,{'Distributed','client,',},[2,1,4]) 
# q = tuple[4]
# q.append(10)
# # print(q , tuple , li)

# # def new_func():
# #     n1 = 3
# #     n2 =  50
# #     q = n2/n1
# #     print(f' Here the value of {n2} divided by {n1} is {q:.3f}')
# #     print(format(q, '.3f'))
# #     print(round(q,3))

# #new_func()

# #local and global variable
# # x = 20
# # def outer():
# #     global x 
# #     y = 20
# #     x += y
# #     def inner():
# #         global x
# #         val = x // 7
# #         x = val
# #         print(val)
# #     inner()
# # outer()
# # print(x)

# #Concatenating of list
# li = [2,3,3]
# li.extend([9,3,2])
# q=li.sort()
# print(li,q)

# a = {2,3,2,4,6}
# b ={2,3,4,1,5,6}
# print(a.issubset(b)) # a is contained in b
# print(a.issuperset(b)) # b is contained in a
# print(a.union(b)) # combine both a and b
# print(a.intersection(b)) # common in both a and b
# print(a.difference(b)) # present in a but not in b
# print(a. isdisjoint(b)) # If a and b have no any common element True else False.



# a = [3,4,("gadget", "oragan")]
# b = [1,5,("medrian","DBMS")]
# q=zip(a,b)
# print(a,b)
# for i,(a,b) in enumerate(zip(a,b)):
#     print(i, (a,b))

# name = ["Alok", "Shree"]  # it takes correspond element of same index
# f = ["Yadav","Ram"]
# for i in zip(name , f):
#     print(i)

# a = list(input("Enter the name of hardware :").split())
# #b = list(input("Enter the name of software :"))
# dic ={}
# for i , v in enumerate(a):
#     dic[i] = v
# print(dic)

#finding the smallest number

val = {-4,-15,-21}

#small =val.pop() # for only valid positive intrger
print(max(val))
         
      
# def table(n):
#     for i in range(1 , 11):
#         table = n*i
#         print(table , end=' ')
# table(5)


# def multiplicationTable(N):
#     #code here 
    
#     for i in range(1 , 11):
#         table = N * i
#         print(table , end=' ' )

# def stringJumper(s):
#     length = len(s)
#     for i in range(length):
#         if i %2 == 0:
#             print(s[i])
# stringJumper('Hello')

# a = 'Hello'
# b = 'World'
# print(a+b)  

# str = input()
# integer = int(input())
# floating = float(input())
# a = integer +10
# b = floating * 10
# print(str, '\n', a, '\n', b)
# print(a)
# print(b)  
    
=======
# #Basic slicing
# #q = 'The most genuine programming language is Python'
# # print(q[:-4]) 

# #Extebded slicing
# # num  = '1 3 4 5 6 7 8 9'
# # print(len(num))
# # print(num[3::3])
# # print(num[-4::10])
# # print(num[7::-10])

# #Start , end , step
# # a = 'Retrieval Agument Generation'
# # print(a[:5:1])
# # print(a[:0:2])
# # #print(a[::0])#cannot have step as 0
# # print(a[3:6:9])

# #sclicing in a list
# # lst = [1,2,3,4,5,6,7,8,9]
# # print(lst[:8:3])

# str = 'My journey in my coding is clear'
# # q=str.replace('My','Explicitly')
# # l=len(q)
# # print(q , str[::-1])
# # upper =  str.upper()
# # lower = str.lower()
# # print(upper , lower)
# # print(str.center(100))
# # w = str.count('a')
# # if w == 1:
# #     print(f'There is {w} occurance of a')
# # else:
# #     print('none')
# print(str.isdigit())
# print(str.isalpha())
# print(str.strip())
# print(str.split())
# print(''.join(reversed(str)))

# print(list(str))
# print(tuple(str))
# print(set(str))


# li =  ['apple', 'dragon fruit' ]
# print(li.count('apple'))
# print(li.index('apple'))


#dictionary
# str = 'Database is a collection of interrelated data'
# dict = {}
# for i in str:
#     if i in dict:
#         dict[i] += 1
#     elif i == '':
#         continue
#     else:
#         dict[i] = 1
# print(dict)


# li = [1,2,[3,4],5,6,[7,8,9]]
# print(li[2][-1])
# tuple = (3,5,6,{'Distributed','client,',},[2,1,4]) 
# q = tuple[4]
# q.append(10)
# # print(q , tuple , li)

# # def new_func():
# #     n1 = 3
# #     n2 =  50
# #     q = n2/n1
# #     print(f' Here the value of {n2} divided by {n1} is {q:.3f}')
# #     print(format(q, '.3f'))
# #     print(round(q,3))

# #new_func()

# #local and global variable
# # x = 20
# # def outer():
# #     global x 
# #     y = 20
# #     x += y
# #     def inner():
# #         global x
# #         val = x // 7
# #         x = val
# #         print(val)
# #     inner()
# # outer()
# # print(x)

# #Concatenating of list
# li = [2,3,3]
# li.extend([9,3,2])
# q=li.sort()
# print(li,q)

# a = {2,3,2,4,6}
# b ={2,3,4,1,5,6}
# print(a.issubset(b)) # a is contained in b
# print(a.issuperset(b)) # b is contained in a
# print(a.union(b)) # combine both a and b
# print(a.intersection(b)) # common in both a and b
# print(a.difference(b)) # present in a but not in b
# print(a. isdisjoint(b)) # If a and b have no any common element True else False.



# a = [3,4,("gadget", "oragan")]
# b = [1,5,("medrian","DBMS")]
# q=zip(a,b)
# print(a,b)
# for i,(a,b) in enumerate(zip(a,b)):
#     print(i, (a,b))

# name = ["Alok", "Shree"]  # it takes correspond element of same index
# f = ["Yadav","Ram"]
# for i in zip(name , f):
#     print(i)

# a = list(input("Enter the name of hardware :").split())
# #b = list(input("Enter the name of software :"))
# dic ={}
# for i , v in enumerate(a):
#     dic[i] = v
# print(dic)

#finding the smallest number

val = {-4,-15,-21}

#small =val.pop() # for only valid positive intrger
print(max(val))
         
      
# def table(n):
#     for i in range(1 , 11):
#         table = n*i
#         print(table , end=' ')
# table(5)


# def multiplicationTable(N):
#     #code here 
    
#     for i in range(1 , 11):
#         table = N * i
#         print(table , end=' ' )

# def stringJumper(s):
#     length = len(s)
#     for i in range(length):
#         if i %2 == 0:
#             print(s[i])
# stringJumper('Hello')

# a = 'Hello'
# b = 'World'
# print(a+b)  

# str = input()
# integer = int(input())
# floating = float(input())
# a = integer +10
# b = floating * 10
# print(str, '\n', a, '\n', b)
# print(a)
# print(b)  
    
>>>>>>> aa2e7dcd15f91be88c03e886b9e67eae8692673b
    