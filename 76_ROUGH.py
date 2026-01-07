# s = ("")
# s += 'retrieval augmented generationretrieva'
# q = s.split()
# print(q)

# a = [12,3,5,1,2]
# b = [7,8,9]
# a.sort(reverse=True)
# #a.extend(b)
# print(a)


# a = [1,2,3,4,5]
# print(a[-2:])
# 
# i = 0
# while i<=10:
#     i += 1
#     if i == 3:
#         continue  # skip all value and execute the loop 
#     print(i)
    
# q = [1,3,4,5,[1,3,4,5]]
# a = [1,3,4,5]
# if a in q :
#     print('True')

# import captcha
# print(captcha.captcha_gen())

# a = 'retrieval'
# if isinstance(a,str):
#     print("yes")

# print(len("12312"))
# print('123'.isdigit())

# message = 12_000_000  #in integer for larger number write using underscore(_)
# print(message)


# var = 6
# var = 'Generative AI'
# print(var)

# import this
# li = [4,5,8,3,1,2]
# q = li.pop(3)
# li.insert(4,9)
# li.remove(4)
# li.insert(1,15)
# li.remove(1)
# li.sort(reverse=True)#  is python defined method reverse into decending order
# li.sort()
# print(li)
# print(sorted(li))
# print(li)


#Reverse in sorted order
# arr = [23,45,64,90,89,24,80]
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] < arr[j]:
#             arr[i] , arr[j] = arr[j] , arr[i]
# print(arr)

# for i in range(1,len(arr)+1):
#     rev = arr[len(arr)-i]
#     revs.append(rev)
# print(revs)
# li = [i for i in range(1,5)]
# li = list(range(1,10))
# print(li[-5:3])
# print(len('                                    '))


# i = (['rag']).title()
# print(i)
# a = {2,2,3,4,5}
# b = {5,2,6,7,4}
# print(b^a)

# a = 40
# a = abs(a)
# print(int((str(a))[::-1]))

# import random
# s = random.randint(0,100)
# a = s
# print(a,s)

# a = {1}
# list(a)[0] = 5
# print()

# a = 50.00//2
# print(a)

# from cap.Guess import run
# run()


# n = [1,2]
# li = [['Data','Proposal'],
#       ['Security','Encryption']
#     ]

# dic = {}
# for i in range(len(li)):
#     dic[n[i]] = li[i]
# print(dic)



s = 'BANANA'
print(s.count('AN'))
# s = 'BANANA'
# print(s.count('AN'))


# print("234".isdigit())



# item = {

#     "Bhagavad Gita": 
#         {"Price":20, #price
#         "Quantity":10,  #Quantity
#         "Sold":6, #sold
#         "Status":"In Stock"},

#     "The Lord of the Rings": 
#         {"Price":45,
#         "Quantity":12,  #Quantity
#         "Sold":6, #sold
#         "Status":"In Stock"}
    
# }
# print(item["Bhagavad Gita"]["Price"])

# rows = []
# for key,val in item.items():
#     rows.append([key,val[0],val[1],val[2],val[3]])
# print()

# for i,row in enumerate(rows):
#     print(f"{i+1}.",end='')
#     for value in row:
#         print(f"{value:<32}",end='')
#     print()
# print('⁃'*150) 

# for i,(key,value) in enumerate(item.items(),start=1):
#     print(f"{i}.{key}")
#     for k,v in value.items():
#         print(f"{k}: {v}")
#     print()

# try:
#     y = 1/0
#     print(round(y,2))
# except:
#     print(False)
    

# import time
# while True:
#     user = input("Let's chat with me...")
#     time.sleep(1.0)
#     print("Thinking...")
        
#     for _ in range(100):
#         time.sleep(1.2)
#         print("Installing virus in your system...")
#         time.sleep(1.5)
#         print("Download completed!")
#         print()

# import Vector

# a = (2,3,4)
# b = (2,3,5)

# v1 = Vector.Vector(a)
# v2 = Vector.Vector(b)

# print((v1+v2))
# print((v1-v2))
# print(v1*v2)

# class Solution:
#     def __init__(self):
#         self.book = {"Bhagwat Gita":"The Hobbit"}
        
# s = Solution()
# s.book["Rich Dad"] = "Author"
# print(s.book)


# a,b = list(map(str,input().split()))
# print(a)
# print(b)





# li = [
#     {
#         "b":[{"pass":'2323', "word":345},  
#              {"pass":'2390', "word":345}]
        
#      }
# ]
# for o in li:
#     for i in range(len(o['b'])):
#        print(o["b"][i]["pass"][2:])
        


# a = {
#     1:'alao',
#     2:'ballo'
# }
# m = max(a.keys())
# print(m)

# from datetime import datetime, timedelta
# t = (datetime.today()).time()
# print(t)

# div = 12988.34
# print(round(div, -2))
# print(all((True,False)))
# print((True + True + True))

# x = 2.5
# print(x.as_integer_ratio())

# a = [1,2]
# def f(a):
#     return  a[1] if len(a) >=3 else None
# print(f(a))

# l = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']

# print(l[(len(l)//2)+1: -1])
# print(len([]))
# print([1,2,3] > 2)

# import random
# possible_outcome = []
# for _ in range(1):
#     possible_outcome.append(random.randint(1,6))
# print(possible_outcome.count(1), possible_outcome.count(2), possible_outcome.count(3), possible_outcome.count(4), possible_outcome.count(5), possible_outcome.count(6))


# a = "Cainoville".lower()
# print('casino' in a)


# doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
# keywords = ['casino', 'they']
# dic = {}
# for i, doc in enumerate(doc_list):
    
#     tokens = doc.split()
#     normalized = [token.strip(",.").lower() for token in tokens]

#     for key in keywords:
#         if key.lower() in normalized:
#             if key.lower() not in dic:
#                 dic[key] = [i]
#             else:
#                 dic[key].append(i)
#         else:
#             if key.lower() not in dic:
#                 dic[key] = []

# print(dic)

# import math
# print((math.log(4,2)))
# # print(dir(math))
# print(math.factorial(5))


# from math import *
# print(sin(90), log(10,10))

# from numpy import *
# print(random.randint(low=1, high=6, size=1))


# LCGs = Linear Congurencial Generators
# Formula: Xₙ₊₁ = (a · Xₙ + c) mod m

# import random
# class RandomGenerator:
#     # Seed: Initial or stating value
#     def __init__(self, seed=1):
#         self.X = seed    # X -> State 
    
#     def next(self, a, c, m=2**31):
#         # a ->  # multiplier
#         # c -> # Increment
#         # m -> # module
        
#         self.X = (a * self.X + c) % m
#         return self.X

# class Biased(RandomGenerator):
#     def winning_chance(self):
#         probabilities = (
#             [1]*1 +
#             [2]*2 +
#             [3]*5 +
#             [4]*2 +
#             [5]*1 + 
#             [6]*5
#         )
        
#         prices = {
#             1:'$5',
#             2:'$1',
#             3:'$0',
#             4:'$1',
#             5:'$5',
#             6:'$0'
#         }
        
#         index = self.next(a, c) % len(probabilities)
#         n = probabilities[index]
#         return f"{prices[n]}"

# rng = Biased()

# a = random.randint(100, 100000)
# c = random.randint(100, 10000)
# rng.next(a, c)
# player = f"You won {rng.winning_chance()}"
# print(player)

# from numpy import *
# rolls = random.randint(low=1, high=6, size=10)

# print(rolls >3)


# # creates 2D matrix
# arr = [[1,2], [3,4]]
# m = array(arr)

# print(f"{arr}\n {m}")  #Use f-string
# print("_"*100)
# print("{}\n {}".format(arr, m))  #use format-string

# import numpy
# print(len(dir(numpy)))

# print(['K','K', '2'] > ['3'])


# with open("words.txt")as f:
#     print((f.read()).split('\n'))

import re
s = "1000_words.txt"
k = "01_lling.log"
if re.compile(r'^(\d{1})').match(k) and '0':
    match = (re.compile(r'^(\d{2})').match(k))
    if match:
        print(True, int(match.group(1)))

# import os
# print("1000words" in os.path.splitext(s))