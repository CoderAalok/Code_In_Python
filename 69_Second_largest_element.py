#  Method-I

# def second_largest_element(arr):
#     if not arr:
#         return None
    
#     i = 1
#     while i != len(arr):
#         if arr[i-1] < arr[i]:
#             t = arr[i-1]
#             arr[i-1] = arr[i]
#             arr[i] = t
            
#             i = 1
#         else:
#             i += 1
#     return arr[1]
   
   

#  Method-II

# arr = [12,3,90,34,65,43]
# # print(second_largest_element(arr))
            
# def SLN(arr):
#     arr = sorted(arr, reverse=True)
#     return arr[1]
# print(SLN(arr))



# Method-III
# Better than other this approach
# Time Complexity: O(n)
# Axuiliry Speed: O(1)

def second_largest_element(arr):
    if not arr or len(arr) < 2:
        return None
    
    largest = second = -1
    
    for n in arr:
        
        if n > largest:
            second = largest
            largest = n
            
        elif second < n <largest:
            second = n
            
    return second

arr = [0,1,3,5,3,3,66,5,5,7,7,8,8,9,9,0,7,4]
print(second_largest_element(arr))