# s = 'python'
# # for i in s:
# #     print(i)
# a = 'h'
# # # print(set(s))
# if a in s:
#     print(True)

# s = {1:2,3:4}
# a = min(s.values())
# print(a)


# s = 'python@'
# print(isinstance(s,str))
# print(s.isalpha())



# import string

# special = ";"
# if special in string.ascii_letters:
#     print("True")

# k = ""
# s = 'python'
# a = 'Encapsulation'
# for i,j in zip(a,s):  #python interpreter only minimum possible character print
#    k += i + j
   
# print(k)

# dic = {'s':3 , 'a':9 }
# a = max(dic.values())  #It gives maximum value
# a = max(dic, key = dic.get)  #It gives maximum value of its' key
# print(a)

# s= 's'
# print(s.isalpha())
# vars

# def f():
#     for i in range(10):
#         yield i+1  #yield function execute infinite time repeate single value but not itself  and itself resume

# for _ in range(3):
#     print(next(f()))

# Sum of all values 
# dic = {'Hard Disk':5000, 'RAM':2000, 'USE':1000}
# val = tuple(list(dic.values()))
# #Method-I
# print(sum(val))

# #Method-II
# sum_ = 0
# for i in val:
#     sum_ += i
# print(sum_)

# #Method-III
# addition = 0
# i = 0
# while i != len(val):
#     addition += val[i]
#     i += 1
# print(addition)


# OS = {'Floppy Disk': '500MB',
#       'Pen Drive':'32GB',
#       'CD/DVD': '1000MB',
#       'Smart Media': '256MB'
# }

# Method-I
# # del OS['Floppy Disk']
# print(OS)

# Method-II
# res = [[k,v] for k , v in OS.items() if v <'500MB']
# print(res)

# Method-III
# OS.pop('Floppy Disk')
# print(OS)
# add = (OS.get('Memory','Memory'))
# OS[add] = '16GB'
# print(OS)

# Method-I (Time Complexity: O(n))
# li = [{'Apple':300}, {'Banana':100}, {'Coconut':200}]
# for i in range(1,len(li)):
#     q,k = li[i-1] , li[i]
#     valQ = list(q.values())
#     valK = list(k.values())
#     if valK[0] < valQ[0]:
#         li[i],li[i-1] =li[i-1], li[i]
# print(li)

# Method-II
# List inside dictionaries using itemgetter 

# from operator import itemgetter

# Ways to sort list of dictionaries by values Using itemgetter

# li = [{"Name":"Walnut", "Price":1800},
#       {"Name":"Cashew", "Price":1500},
#       {'Name':'Apple','Price':300},
#       {'Name':'Banana','Price':100}, 
#       {'Name':'Coconut','Price':200}
#     ]
# result = sorted(li, key=itemgetter("Price"))
# print(result)
# ----------------------------------------------------------------

# Ways to sort list of dictionaries by values Using lambda function

# li = [{"Name":"Walnut", "Price":1800},
#       {"Name":"Cashew", "Price":1500},
#       {'Name':'Apple','Price':300},
#       {'Name':'Banana','Price':100}, 
#       {'Name':'Coconut','Price':200}
#     ]
# result = sorted(li, key=lambda i: i['Price'])
# print(result)
# -----------------------------------------------------------------

dict1 = {'Hacking':'Fishing', "Malicious":'Farewell'}  #dictionary itself negelete duplicate keys and values
dict2 = {"Malicious":'SwitchCase', "Interupt":'DATA'}
# Merging two Dictionaries
# Method-I
# dict1.update(dict2)
# print(dict1)

# # Method-II
# for key,value in dict2.items():
#     dict1[key] = value
# print(dict1)

# Method-III
# res = {**dict1,**dict2}
# print(res)

# # Method-IV
# result = dict1 | dict2
# print(result)
# ---------------------------------------------------

# Convert key-values list to flat dictionary
# li = list(dict1.items())
# # Method-I
# result = dict(li)
# print(result)

# # Method-II
# dic = {}
# for i in range(len(li)):
#     dic[li[i][0]] = li[i][1]
# print(dic)
# --------------------------------------------------

#Insertion at the beginning in OrderedDict
# Method-I (RAW logic)
# dic = {
#     "Linear Algebra":"Matrix",
#     "Calculas":"Differential Equation",
#     "Probability":"Statices"
# }
# l = len(dic)
# dic["Permutation"] = "Combination"
# dic.update({"Complex":"Cube Root", "Binomial Therome":"Mathematical Principal"})
# li = list(dic.items())
# print(li)
# res = li[l:] + li[:l]
# res = dict(res)
# print(res)

# Method-II
# from collections import OrderedDict

# dic = OrderedDict([("Linear Algebra","Matrix"),("Calculas","Complex Number")])
# dic.update({"Permutation":"Combination"})
# dic.move_to_end("Permutation",last=False)
# print(dic)

#Check order of character in string
# strr= "dettox"
# par = "tt"
# print(par in strr)

# def order(strr,pattern):
#     if not strr and not pattern:
#         return None
#     k = 0
#     for ch in strr:
#         if ch == pattern[k]:
#             k += 1
#             if k == len(pattern):
#                 return f"'{pattern}' character order matched in string '{strr}'."
#         else:
#             k = 0
#     return -1
# # Method-I
#     # T= 0
#     # for i in range(len(strr)):
#     #     if strr[i] == pattern[T]:
#     #         T += 1
#     #         if T == len(pattern):
#     #             return (f"'{pattern}' character order matched in string '{strr}'.")
#     #     else:
#     #         T = 0
#     # return -1
# strr= "detttox"
# pattern = 'at'
# print(order(strr,pattern))

# li = input().strip()
# print(li)

# li = [1,34,5,6,7]
# li.sort()
# li.pop(2)
# print(li)

# l = (input().strip())
# print()

# l = '2 0 4'
# a = (2,3,4)
# if all(int(i) in a for i in l.split() if i != '' ):
#     print(True)
# else:
#     print(False)

# n = int(input())
# t = tuple(map(int,input().strip().split()))

# print(hash(t))
# print(hash((1,2)))








# from itertools import permutations
# li = 'HACK'

# re = sorted(list(permutations(li,2)))
# print(re)
# result = [list(t) for t in re ]
# for ch in result:
#     print(''.join(ch))
# from itertools import permutations

# def arrange(strr,r=2):
    
#     re = sorted(list(permutations(strr,r)))
#     result = [list(i) for i in re]
    
#     for ch in result:
#         print(''.join(ch))

# strr= input().strip()


# arrange(strr,r) 

# s = map(input())
# print(s)
# strrInt = input().strip().split()
# print(strrInt)
# def permutation(arr):
#     # Base Condition
#     if not arr:
#         return []
    
#     if len(arr) <= 1:
#         return [arr]
    
#     # ---Main Approach---
#     result  = []
#     for i in range(len(arr)):
#         hold = arr[i]
#         rearrange = arr[:i] + arr[i+1:]
#         for ch in permutation(rearrange):
#             result.append(hold + ch)
#     return result

# print(permutation('asd'))


# def f(a):
#     c = list(range(len(a)))
#     c = list(range(3,0,-1))
#     return c
# print((f('asd')))    


# Dictionary to find mirror characters in a string
# def mirror(strr,n):
#     if strr.strip() == ""  or  n<0:
#         return None
    
#     alpha = 'abcdefghijklmnopqrstuvwxyz'
#     rev = alpha[::-1]
#     dictchar = dict(zip(alpha,rev)) #make dictionary of mirror characters both string
    
#     prefix = strr[:n-1]
#     surfix = strr[n-1:]
#     mirror = prefix
    
#     for i in range(len(surfix)):
#         mirror += dictchar[surfix[i]]
#     return mirror

# print(mirror('paradox',3))

# def mirror(strr,n):
#     if strr.strip() == ""  or  n<0:
#         return None
    
#     alpha = 'abcdefghijklmnopqrstuvwxyz'
#     rev = alpha[::-1]
    
#     prefix = strr[:n-1]
#     surfix = strr[n-1:]
    
#     mirror = str.maketrans(alpha,rev)
#     return    prefix + surfix.translate(mirror)
    
# print(mirror('paradox',3))

#  *n, m = input().split()
# print(n)
# print(m)

# a = dict([(1,2),(3,4)])
# print(a)

# if any(i in "alok" for i  in {"@","!"}):
#     print(True)

# s =  "The programm  ing"
# print(s.replace(" ",""))

# from collections import defaultdict

# dic = []
# default = {}
# # default["python"].append('language')
# # default["python"].append('High proformance')
# default.setdefault('python',[]).append("high proformance")
# default.setdefault("python",[]).append("languange")
# print(default['python'])

# dic.append(default)
# print(dic)
# arr = []
# if not arr:
#     print(True)
#     # exit()
# if not arr:
# #     print(False)

# li = [1,2]
# no = []
# for i in li:
#     if i == 1:
#         li.remove(i)
#         print(li)
#         break
# no.append(None)
# print(no)
# print(li)
# li.remove(1)
# # del li[0]
# # del li[0]
# print(li)
# li.append((3,4,1,2))
# print(li)

# import datetime,time
# d= (datetime.date(2025,12,14))

# print(d.year, d.month, d.day)
# print(d)
# 
# 
# from datetime import datetime, timedelta, date
# from time import sleep

# strr = '2005-01-05'
# strr1 = '2005-01-10'
# d = datetime.strptime(strr, "%Y-%m-%d")
# s = datetime.strptime(strr1, "%Y-%m-%d")

# print((s-d).days)
# print(type(d))

# print(date.today())
# time_ = []
# s = date.today()

# time_.append(str(s))
# c = s+timedelta(days=20)
# time_.append(str(c))
# print(time_)


# print(datetime.now())
# sleep(2.0)
# print(datetime.now())


# import time

# def file(strr, default=[]):
#     (default.append(strr))
#     print(f"{datetime.now()} {default}")
# file("Python")
# sleep(2.0)
# file("Program")


# def file(strr, default=None):

#     if default is None:
#         default = {}
#         default[strr] = datetime.now()
#         return default
    
#     # return default

# print(file("Python"))
# sleep(2.0)
# print(file("Program"))


# li = [{"python":[2.14, 2.33, 2.55]}, 
#       {"Hard":"code"},
#       {"Graphic":"Ultra"}
#       ]
# for l in li:
#     if 'python' in l:
#         break
# k = l['python'][2]
# del l['python'][2]
# print(li) 
# print(k)

# dic = {}
# dic["Python"] = [2.14,2.55,2.90,3.14]

# print(dic)
# del dic["Python"][2]
# print(dic)

# li = [1,2,3,4]
# print(li.index(2))

# u = [1,2]
# # for i in u:
# #     print(None)

# ui = [8,7]
# a = None
# b = True
# try:
#     if not a or not b:
#         raise Exception("Not True") 
    
# except Exception as e:
#     print(e)

# def fun(y):
#     return fun1(y)

# def fun1(x):
#     return x**5

# print(fun(2))

# from datetime import  timedelta, date

# d = "2005-2-9"
# print(date.strptime(d, "%Y-%m-%d") + timedelta(days=5))

# a = b = None
# print(a,b)
# if (a or b) is None:
#     print(True)
# print(datetime.today())
# s =  "python"
# confirm = False
# while not confirm:
#     u = input()
#     if u == s:
#         confirm = True
#     else:
#         print("Wrong")


# li = [1,2,3,4]
# li1 = [20,8,5]
# while True:
#     a = int(input())
#     if a in li:
#         print(True)
        
#     elif a in li1:
#         print("True1")
#         break
#     else:
#         continue
# print("Done")


# e = next((n for n in li if n == 4),None)
# print(e,li.count(5))


# s = "Python is best programming language".replace(" ","")
# if s.isalpha():
#     print(True,s)


# import uuid
# order = (uuid.uuid6())
# print((order))




# def inc(order_id):
    
#     numb = (int(order_id["order_id"][3:])) + 1 
#     order_id["order_id"] = f"UoB{numb}"
#     return  order_id["order_id"] 

# # print(order_id)
# order_id = {"order_id":"UoB100"}

# print(inc(order_id))
# print(inc(order_id))

# print(order_id)


# ser_record = [
#             ("UserID", 3142),
#             ("book_id", [3142]),
#             ("order_id", [3142]),
#             ("borrow_date", str(date.today())),
#             ("status", "PENDING")
#         ]
# dic = dict(ser_record)
# dic['book_id'].append("python")
# print(dic)

# maxid = 0
# li = [["uob100","uob101"],['uob102','uob103'],['uob104','uob105']]
# liid = []
# for val in li:
#     liid += val
# for l in liid:
#     maxo = int(l[3:])
#     maxid = max(maxid, maxo)
# maxid += 1
# latestid = f'uob{maxid}'
# print(latestid)


# li = [1,2,3,4,5]
# for i in li:
#     li.remove(i)
#     print(li)
# print(li)

# t = '2005-02-02'
# print(t+ timedelta(days=5))
# li = []
# # val = [i for i in li if i == 2]
# val = next((i*2 for i in li if i==8),None)
# if val is None:
    
#     print(val)
    
    
# import json
# filename = "Book_borrow.json"
# try:
#     with open(filename, "r")as f:
#         json.load(f)
# except FileNotFoundError:
#     default = []
#     print(default)

# while True:
#     u = input()
#     if u == 'q':
#         quit()
# print(list(range(10)))

# k = 3

# d  = dict([('a',k), ('b',1)])
# for i in d:
#     if not i:
#         print(False)
#         break

# from datetime import datetime, timedelta

# t = (datetime.now()).strftime("%H:%M:%S")
# s = ((datetime.now()) + timedelta(minutes=5)).strftime("%H:%M:%S")
# print(t<s, t,s)


# import os 
# files = os.listdir()
# for i, file in enumerate(files, start=1):
#     f, ext = os.path.splitext(file)
#     print(ext)
# print(".python".strip('.'))
# start = '00'
# for i in range(1,20):
#     n = len(list(str(i)))
#     if n < 2:
#         print(start[0] + str(i))
#     else:
#         print(str(i))

# for i in range(1, 100):
#     print(f"{i:02}")



