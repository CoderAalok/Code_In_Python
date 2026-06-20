#map() function : A function which applies to each elements of an iterable and
# return iterator object or map object.

# li = [2,3,4]
# li1 = [1,3,5]
# res = map(lambda x,y: x*y if y>1 else 0,li,li1)
# res1 = max(map(lambda x: x,li1))
# print(res1)
# print(list(res))

# n1,n2 = map(int,input().split())
# print(n1,n2)

# li  = ["OOP","Computer Network","DBMS","Operating System"]
# res = list((filter(lambda x: x if len(x)>5 else 0 ,li)))


# print(res)

# def fun(x):
#     return x if x%2 != 0 else 0

# li = [1,2,3,0]
# re = filter(fun,li)
# print(list(re))

# print(list(filter(fun,[1,2,4,6])))



# def fact(x):
#     return x>5

# print(set(filter(fact,[2,1,6,8,0,5])))

# s = 'python fun to code'

# res = map(list,s.split())
# print(list(res))

# re = "".join(list(input().strip()))
# print(re)
# def fun(x):
#     return x%2 != 0
# li = [2,3,15,6]
# re = map(fun,li)
# print(list(re)) # output: Boolean type return because passing into condition 

# def fun(x):
#     return x*2
# li = [2,3,15,6]
# re = map(fun,li)
# print(list(re))  #list of integer


# li = ["Graphic  ", "Quantum    ","Artificial  "]

# res = list(map(str.strip,li))
# print(res)
# result = set(map(lambda x: x[0],li))
# ==================================================================================================
# print(result)

# a = (2,3,-4,3,-1)
# b = (1,-9,0,1,-5)

# # Multiple times call, each call gives value 
# def fun(a,b):
#     re = [i+j for i,j in zip(a,b)]
#     return re
# print(tuple(fun(a,b)))
# print(set(fun(a,b)))

# print()
# # After call one type of function then not execute other one
# re = map(lambda x,y: x+y,a,b)
# print(list(re))
# print(tuple(re))
# print(set(re))


