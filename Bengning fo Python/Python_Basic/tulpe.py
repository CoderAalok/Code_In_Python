tuple = (2,3,53,5,7,3)
del tuple(6)
print(tuple)


# tup = (12,23,345)
# print(len(tup))

# Find maximum and minimum K elements in tuple
# t = (12,3,1,2,5,10,6,7,8)
# k = 4

# """
#     max:k=2-elements
#     min:k=2-elements
# """
# t = sorted(t)
# max_li = sorted(t[-k:],reverse=True)
# # max_li = t[len(t)-k : len(t)]
# min_li = t[:k]

# print(max_li,min_li)
# ------------------------------------------------------------------------------------------------

# def tup(tpl,k):
#     if not tpl or not k:
#         return
    
#     li = list(tpl)
#     li_max = []
#     li_min = []
#     for _ in range(k):
        
#         max_no = max(li)
#         li_max.append(max_no)
#         min_no = min(li)
#         li_min.append(min_no)
        
#         li.remove(max_no)
#         li.remove(min_no)
    
#     return li_max,li_min

# liMax,liMin = tup(t,k)
# print(f"{liMax}\n {liMin}")
# ---------------------------------------------------------------------------------------------

# Find list of tuple from given list numbers and each of its cube
# li = [2,4,5,6,8]

# li_tuple = []
# for i in li:
#     n = i**3
#     li_tuple.append((i,n))
# print(li_tuple)

# --------------------------------------------------------------------------------------------------

# Adding 
# t = (1,3,5,7,9)
# li = [0,2,4,6,8]

# t += tuple(li)
# li += list(t)

# print(t,li)

# -------------------------

# Closest Pair to Kth index element in Tuple
# Given a list of tuples and a target tuple, 
# the goal is to find the tuple whose Kth element is closest to the Kth element of the target tuple. 
# Optionally, a threshold K can define the maximum allowable difference. For Example:

# li_tuple = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)] 
# target_tuple = (17,23)
# k = 1  #kth index element  

# def closest_pair(li_tuple,target_tuple,k,threshold=0):
#     target_val = target_tuple[k]
    
#     min_diff = float('inf')
#     closest = None
    
#     for t in li_tuple:
#         diff = abs(t[k] - target_val)
        
#         if diff < min_diff and diff >= threshold:
#             min_diff = diff
#             closest = t

#     return closest 
# print(closest_pair(li_tuple,target_tuple,k))


# li_tuple = [(3, 4), (19, 20),(78, 23), (2, 3), (9, 8)] 
# target = (17,23)
# k = 1  #kth index element 

# minval = float("inf")
# closest = []
# threshold = 0

# for t in li_tuple:
#     diff = abs(t[k] - target_tuple[k])
    
#     if diff < minval and diff <= threshold :
#         minval = diff
#         closest.append(t)

# print(closest)



# class Solution:
#     @staticmethod
#     def closest_pair(li_tuple,target,k,threshold):
#         min_val = float('inf')
#         closest = []
        
#         for tup in li_tuple:
#             diff = abs(tup[k] - target[k])
            
#             if diff <= threshold:
                
#                 if diff < min_val:
#                     min_val = diff
#                     closest =  [tup]  # previous reset
                
#                 elif diff == min_val:
#                     closest.append(tup) 
                
#         return closest
                

# li_tuple = [(3, 4), (19, 20),(78, 23), (2, 3), (9, 8)] 
# target = (17,23)
# k = 1
# result = Solution()
# res = result.closest_pair(li_tuple,target,k,3)
# print(res)



# li = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
# res = [tuple(set(li[i-1]+li[i])) if li[i-1][0] == li[i][0] else li[i] for i in range(1,len(li)) ]
# print(res)


# li = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
# li = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]

# mapping = {}
# # Method-I
# for (k,v) in li:
#     mapping.setdefault(k,[]).append(v)  # setdefault ->> {key:[val]}
# result = [(key,*val) for key,val in mapping.items()]
# print(result)

# # Method-II
# li = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
# mapping = {}

# for i in li:
#     mapping[i[0]] = mapping.get(i[0],[]) + list(i[1:])

# result = [(k,)+tuple(v) for k,v in mapping.items()]
# print(result)


# Extract digits from list of tuple or tuple list

# li = [(15,31),(12,43,0)]

# nums = [n for i in li for n in i ]

# digits = set()
# for num in nums:
    
#     if num == 0 :
#         digits.add(num)
    
#     while num != 0:
#         dig = num%10
#         digits.add(dig)
#         num = num//10
        
# print(sorted(digits,reverse=True))


# li = [(1,2,4,5),(3,2,3,4),(3,4,2),(1,3,5,6,3),(4,21),(9,0),(12,3),(1,4)]
# k = 2
# result = list(filter(lambda x : len(x)!=k,li))
# # result = [i for i in li if len(i) != k]
# print(result)

# # ____________________________________________________________________________
# Sort a list of tuple based on their second item/element, 
# But condition: ordered data of tuple holds

li = [(1,3),(3,4),(5,3)]
k = 1
sort = sorted(li, key=lambda x: x[k])
print(sort)

#t= ()
#z=int(input())
#t=t+(z,)
#x=int(input())
#if x in t:
#   print(t.index(x))
#   
#   
#else:
#   print("False")