#arr=[1,3,5,7]

#target=int(input("Enter your targeted number : "))

#print("The subarray from to  is ", sub_array(arr , target))          



#a=1,3,4,5,4
#print(list(a))
#complex number
#a=1+4j
#b=1-4j
#print(a*4j)

#z=[0,4,6,5,78,93,1,8,8,"LLM" , "RAG"]
#z.sort()
#z.append(0)
#z.insert(0,2)
#z.pop(10)
#z.reverse()
#z.remove("RAG")

a=[1,2,4,5,6]
del a[0]
print(a)
#i=0
#z=len(a)
#sum=0
#t=sum(a)
#print(type(a))
#print(t)
#print(int(len(a)))
#while i< z:
#   sum+= a[i]
#   i+=1
#print(sum)
#   





#z.reverse()
#z.remove("RAG")

a=[1,2,4,5,6]
del a[0]
print(a)
# a=[1,2,4,5,6]
# del a[0]
# print(a)
#i=0
#z=len(a)
#sum=0
print(a)
#   sum+= a[i]
#   i+=1
#print(sum)
#   
#   

# _______________________________________________________________________

# Sort  a list of tuples by second item, tuple order hold
"""
Main idea
key = function applied to each element before comparison
It changes what Python looks at when deciding order, equality, or grouping
The elements themselves don’t change
"""
# Method-I
# li = [(1, 3), (4, 1), (2, 2)]
# result = sorted(li,key=lambda s: s[1])
# print(result)

# # Method-II (Only for  unique elements)
# li = [(1, 3), (4, 2), (2, 2)]
# k = 1#int(input())
# key = {}
# if k <= len(li[0])-1:
#     for i in range(len(li)):
#         key[li[i][k]] = li[i]
# keys = [key[j] for j in sorted(key.keys())]
# print(keys)
# __________________________________________________________________________________________________
# li = ["Global",'Local','lambda','Networking','Fishing','Security']
# res = sorted(li,key=len)  #According to length accending order
# print(res)
# print(sorted(li,key=len,reverse=True))   #According to length deccending order

# print(min(li,key=len))
# print(max(li,key=len))


# li = [1,2,4]
# li.insert(9,3)
# print(li)
# __________________________________________________________________________________________________

# Order Tuples by list
# li =  [('Gfg', 10), ('best', 3), ('Geeks', 7), ('CS', 8)]
# ord_list = ['Geeks', 'best', 'CS', 'Gfg'] 

# Method-I
# for i in range(len(ord_list)):
#     if ord_list[i] != li[i][0]:
#         for j in range(len(li)):
#             if li[j][0] == ord_list[i]:
#                 li[j],li[i] = li[i],li[j]
#                 break
# print(li)

# # Method-II  ✅
# order = dict(li)
# result = [(key,order[key]) for key in ord_list]
# print(result)

#Method-III
# result = sorted(li,key=lambda x: ord_list.index(x[0]))  #key= [3,1,0,2]  -> sorted(key) -> [0,1,2,3]
# print(result)

# Method-IV
# mapping = {key:val for val,key in enumerate(ord_list)}
# result = sorted(li,key=lambda x: mapping[x[0]])  #key= [3,1,0,2]  -> sorted(key) -> [0,1,2,3]
# print(result)


# __________________________________________________________________________________________________

# Flatten tuple of list
# tup = ([5, 6], [6, 7, 8, 9], [3])
# # Method-I
# result = ()
# for val in tup:
#     result += tuple(val)
# print(result)

# #Method_II
# result = sum((tuple(val) for val in tup ),() )
# print(result)    #  ()+(5,6) = (5,6)+(6,7,8,9) =(5,6,6,7,8,9)+(3) = (5,6,6,7,8,9,3) same as Method-I

# # Method-III
# from itertools import chain
# result  = tuple(chain.from_iterable(tup))
# print(result)

# __________________________________________________________________________________________________

tup =  ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))
keys = ['key','value','id']

result = []

# Method-I
for i in range(len(tup)):
    dic = {} 
    for k,t in zip(keys,tup[i]):
        dic[k] = t
    result.append(dic)
       
print(result)

# Method-II
result = [{k:v for k,v in zip(keys,t)} for t in tup ]
print(result)

# Method-III
result = list(map(lambda x: dict(zip(keys,x)),tup))
print(result)