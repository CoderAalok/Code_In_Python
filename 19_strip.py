#1.SUM OF ARRAY

# arr = [1,3,4,2,5,6]
# result = 0
# for i in arr :
#     result += i
# print(result)
# print()
# print(sum(arr))

# def s(arr):
#     sub =  sum(arr)
#     return sub
# arr = [1,3,4,2,5,6]
# print(s(arr))

#2.Largest element in an array
# def s(arr):
#     arr1 = list(set(arr))
#     len_arr = len(arr1)
#     for i in range(len_arr):
#         if arr1[i] == arr1[len_arr - 1]:
#             return arr1[i]
#     return None
# arr = [1,3,4,2,5,6,12,0,16,9,10,2,7]
# print(s(arr))

# arr = [1,3,4,2,5,6,12,0,16,9,10,2,7]
# print(max(arr))


#3.ARRAY ROTATION

# def fun(a):
#     remove = a.pop(0)
#     a.append(remove)
#     return a   
# a =  list(input("Enter your desire integers : ").split())  #[1,2,3,4,5,6,7]
# print(fun(a))
    
#String type>....
# a = input("").strip()
# print(a) 
# #strip() : This function remove white-spaces (initial and end  white-spaces only) .
# #split() : This function used to form list,and inside the list ignorance white-spaces.
# for i in a :
#     print(i,end='' )  


# def fun(arr, index):
#     len_arr = len(arr)
#     if index <= 0 or index > len_arr:
#         return None 
#     temp = []
#     arr1 = arr[::-1]    #arr.reverse()#this may affect the time complexity 
#     n = len_arr -index
#     for i in reversed(range(n)):
#         temp.append(arr1[i])
#     for j  in arr:
#         if not j in temp:
#             temp.append(j)
#     return temp 
# arr = [1,2,3,4,5,6,7,8]
# index = 2
# print(fun(arr,index))


# def rotation(arr, index):
#     len_arr = len(arr)
#     if index <= 0 or index > len_arr:
#         return None
#     rem = arr[index :] + arr[:index]
#     return rem
# arr = [1,2,3,4,5,6,7,8]
# index = 5
# print(rotation(arr,index))

# arr = [1,2,3,5,4,6,7,8]
# arr.insert(5,4)
# print(arr)
# a = list(set(arr))
# print(a)

#4.Python Program to Split the array and add the first part to the end
# Alternative methode:

# def rotate(arr, k):
#     result = arr[k:] + arr[:k]
#     return result
# arr = [2,3,8,4,6,4]
# print(rotate(arr, 2))

#5.Find remainder of array multiplication divided by n

# def rem(arr , n):
#     net = 1
#     for i in arr:
#         net *= i
#     div = net % n 
#     return div
# arr = [1,3,5]
# n = 2
# print(rem(arr , n))

#6.Collatz Sequence...
# def fun(n):
#     m = n
#     while True:  
#         if m % 2 == 0:
#             m //= 2
#             print(m)
#         elif m != 1:
#             m = 3*m +1
#             print(m)
#         else:
#             print(m)
#             return m
# n = int(input("Enter a positive : "))
# print(fun(n))


#7.To check if given array is Monotonic

#>>>extend(): combine or concatenate two or more lists

# def monotonic(arr1): 
#     arr1.sort()
#     for i in range(len(arr1)):
#         for j in range(1,len(arr1)):
#             if i <= j and arr1[i] <= arr1[j]:
#                 return True
#     return False
            
# arr1 = [5,2,3,7,6]
# print(monotonic(arr1))

   
# def is_monotonic(arr1):
#      arr2 = []
#      arr3 = []
#      arr2.extend(arr1)
#      arr3.extend(arr1)
#      arr2.sort()
#      arr3.sort(reverse=True)
#      if arr1 == arr2 or arr1 == arr3:
#         return True 
# print(is_monotonic([1,2,2,3]))
# print(is_monotonic([2,4,4,5]))
# print(is_monotonic([9,8,7,7]))
# def monotonic(arr):
#     if all(arr[i] <= arr[i+1] for i in range(len(arr)-1) )or all(arr[i] >= arr[i+1] for i in range(len(arr)-1) ):
#         return True
# print(f" Monotonic array of decreasing order {monotonic([5,3,3,2])}")
# print(f" Monotonic array of increasing order {monotonic([2,4,6,8,10])}")
# print(monotonic([9,7,5,3]))


#8.Interchange first and last elements in a list
# def inter(arr):
#     q = arr[0:-1]
#     z = arr[-1: ]
#     k = q[1:] + q[:1]
#     return z + k
# print(inter([2,4,6,8,10]))


#Largest Monotonic Sub-array 

# def large_monotonic_subarray(arr):
#     if not arr:
#         return None
#     count_inc , count_dec = 1, 1
#     largest = 1
#     start , end  = 0 , 0
#     for i in range(1,len(arr)):
#         if arr[i] > arr[i-1]:
#             count_inc += 1
           
#             count_dec = 1  #reset decreasing while increasing 
           
#         elif arr[i] < arr[i-1]:
#             count_dec += 1
#             count_inc = 1  #reset increasing while decreasing
#         else :
#             count_inc , count_dec = 1, 1
#         #largest = max(largest , count_inc , count_dec)
#         if count_inc> largest :  #compare stored counter value to estimate size of subarray 
#             largest = count_inc
#             start = i-largest +1
#             end = i
#         if count_dec > largest :
#             largest = count_dec
#             start = i-largest +1
#             end = i
#     return largest , arr[start : end+1]
# print(large_monotonic_subarray([5,7,8,3,2,10]))


# swip two elements in array
# def swip(arr,i,j):
#     s = arr[i]
#     arr[i] = arr[j]
#     arr[j] = s
#     return arr
# arr = [5,6,8,9,1,2]
# i ,j= 2,3
# print(swip(arr,i,j))

# print(5<<3)   #  (n*2^m)   n = 5 , m = 3
# print(10>>3)   # n = 10 , m = 3 where m is divider.
# a=["cholate" , "straberry", "pine","flower"]
# b=["kids", "dolls","human", "men"]
# for i in zip(a,b):
#     print(i,end=' ')

# a = 3
# b = 5
# if (a := b:)  # ':=' walrus operator
#    print(None)

#11.Ways to check if element exists in list
# def exists(arr , k):
#     if k in arr:
#       return True     
# print(exists([0,2,4,6,8,10], 10))

# Reversed of list
# arr = [2,3,4,0,45,5]
# arr1 = []
# for i in reversed(arr):
#     arr1.append(i)
# print(arr1)
# print(arr[::-1])

#Find sum of elements in list
# def product(arr):
#    product = 1
#    for i in arr:
#       product *= i
#    return product

# find smallest and largest number

# def small(arr):
#       # val_small = min(arr)
#       # val_large = max(arr)
#       # return val_small , val_large
#       small1 = arr[0]
#       for i in arr:
#          if small1 > i:
#             small1 = i
#       return small1
# print(small([5,10,2,114,9,6,1]))
#Method-1
# def largest(arr,N):
#    if not arr or len(arr) < N:
#       return None
#    large = []
#    i = 1
#    while i <= N:
#       q = max(arr)
#       large.append(q)
#       arr.remove(q)
#       i += 1 
#    return large
# print(largest([33,3,34,23],2))

#Method-2
# def largest(arr, N):
#     arr = sorted(arr)
#     if not arr or len(arr) < N:
#         return None
#     size = len(arr) - 1
#     large = []
#     for i in range(N):
#         last = arr[size-i]
#         large.append(last)
#     return large
# print(largest([2,4,2,6,4],2))

#Method-3
# def largest(arr, N):
#      if not arr or len(arr) < N:
#         return None
#      large = sorted(arr,reverse=True)
#      return large[:N]
# print(largest([3,2,5,6,8,33],3))

#Even numbers in a list

# def even(arr):
#     Even = [i for i in arr if i % 2 == 0]
#     # for i in arr:
#     #     if i % 2 == 0 :
#     #         Even.append(i)
#     return Even
# print(even([3,5,2,6,34,2]))

# To find LIS (Large Increasing Subsequence)

# def large_increasing_subsequence(arr):
#     start , end = 0 , 0
#     DP = [1]*len(arr)
#     for i in range(1,len(arr)): #next element pick
#         for j in range(i): #previous element pick
#             if arr[i] > arr[j]:
#                 DP[i] = max(DP[i] , DP[j]+1)
          
#     return max(DP)
# arr = [4,5,0,2,8,9,10,11]
# print(large_increasing_subsequence(arr))

# import bisect
# a = [5,2,3,9,7]
# a.sort()
# for i in a:
#     # left element index
#     #value give according to i , i providing integer and it will find it. start from (0) index 
#     q = bisect.bisect_left(a,i) 
#       # right element index 
#     #value give according to i , i provide integer and it will find it. start from (1) index 
#     z = bisect.bisect_right(a,i)
#     print(q)

# a = []
# for i in range(1,11):
#     a.insert(len(a),i)
# print(a)

# import bisect 
# a = [3,1,2,4,6,5]
# b = []
# for i in a :
#     # pick one by one element from 'a' and appending on 'b' with sorting
#     bisect.insort(b , i) 
# print(b)

# a = [4,5,3,5,7,2]
# b = []
# for i in a :
#     b.insert(len(b),i)   # false cannot insort as in order
# print(b)
    
#Largest Increasing Subsequence using Binary search method (O(nlogn))
# import bisect 
# def length(arr):
#     sub = []
#     for i in arr:
#         index = bisect.bisect_left(sub,i)  # 'i' positioning the element inside the sub
#         if index == len(sub):
#             sub.append(i)
#         else:
#             sub[index] = i # replace old index value by new if old value greater 
#     return len(sub)
# print(f"The largest increasing length of subsequence is {length([5,3,7,9,2,0])}")
            

##Largest Increasing Subsequence using  Dynamic Programming approach

# def largest_length(arr):
#     n = len(arr)
#     dp = [1]*n  # Initillized with 1
#     for i in range(1,n):
#         for j in range(i):
#             if arr[i] > arr[j]:
#                 dp[i] = max(dp[i], dp[j]+1)
#     return max(dp)
# print(largest_length([3,4,2,5,6]))


# To finding the Longest Subarray with Sum K, for only positive integer

# def longest_subarray(arr, k):
#     len_arr = len(arr)
#     left = 0
#     sub = 0
#     max_len = 0
#     for i in range(len_arr):
#         sub  += arr[i]
#         while sub  > k:
#             sub  -= arr[left]
#             left += 1
#         if sub == k:
#             max_len = max(max_len ,i+1-left)
#     return max_len
# print(longest_subarray([10,20,5,5,20,5,2,7,1,2,8,1,3,1,],30))

# To finding the Longest Subarray with Sum K, for all negative or non-negative

# def longest_subarray(arr, k):
#     len_arr = len(arr)
#     sub = 0
#     max_len = 0
#     prefix_arr = {} #empty dictionary
#     for i in range(len_arr):
#         sub += arr[i]
#         if sub == k:
#             max_len = max(max_len , i+1)
#         #Differecne of current_sum with existing sum , to check already exist in prefix_map(dictionary)
#         if (sub-k) in prefix_arr:
#             max_len = max(max_len , i-prefix_arr[sub-k]) # Difference current index and (key its value)
#         #if  not sub in prefix then to storing current index with that sub
#         if sub not in prefix_arr:
#             prefix_arr[sub] = i  # Adding on dictionay current_sum (key) and current_index (value)
#     return max_len
# print(longest_subarray([10,-50,80,-25,5,-40 ],60))



# Give an array to find whether given array is monotonic or not

# arr = [3,4,4,55,80]
# count = 0
# if all(arr[i-1] <= arr[i] for i in range(1,len(arr)) or (all(arr[i-1] >= arr[i] for i in range(1,len(arr))))):
#     count = True
# else:
#     count = False
# print(count)

# arr  = [6,9,9,3,2,1,1]
# # count , count1 = 0,0
# count = count1 = True

# for i in range(1,len(arr)):   #O(n)
#     if arr[i] > arr[i-1]:  # increasing order  log(n)
#         count1 = False
#     elif  arr[i] < arr[i-1]:  #decreasing order
#         count = False
# # for i in range(1, len(arr)):
# #     if arr[i] <= arr[i-1]:
# #         count1 += 1
# if count or count1:
# # if count == len(arr)-1 or count1 == len(arr)-1:
#     print("Monotonic")
# else:
#     print('no monotonic')


def monotonic_subarray(arr):
    inc = dec = 1
    max_no = 1
    start = end = 0
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            inc += 1
            dec = 1
        elif arr[i] < arr[i-1]:
            dec += 1
            inc = 1
        else:
            inc = dec =1
    #     max_arr = max(max_arr, inc, dec)
    # return max_arr
        if inc > dec :
            max_no = inc
            start = i - max_no +1
            end  = i +1
        if inc < dec :
            max_no = inc
            start = i - max_no +1
            end  =  i + 1
    return len(arr[start : end])
print(f" The Largest Monotonic Subarray of given array is {monotonic_subarray([1,2,4,0,5,6,7,8])}")
