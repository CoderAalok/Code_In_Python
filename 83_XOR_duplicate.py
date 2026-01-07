@ -0,0 +1,52 @@
# with using XOR operator to find a unique element
# def unique_element(arr):
#     if not arr:
#         return None
#     unique = 0
#     for x in arr:
#         unique ^= x
#     return unique
# print(unique_element([1,2,2,3,3,1,6]))

# def unique_element(arr):
#     if not arr:
#         return None
    
#     # dic = {}
#     unique = []
#     non_unique = set()
    
#     for x in arr:
#         uni = arr.count(x)
#         if uni == 1:
#             unique.append(x)
#         else:
#             non_unique.add(x)
#         # if x not in dic:
#         #     dic[x] = 1
#         # else:
#         #     dic[x] += 1
#     return f"Unique: {unique}, NON-Unique: {non_unique}" #[k for k, v in dic.items() if v == 1]
# print(unique_element([1,1,2,2,3,3,1,4,5,7,8,9]))


# without using XOR operator
# def duplicate_element(arr):
#     if not arr :
#         return None
    
#     seen = set()
#     non_unique = set()
#     for x in arr:
#         if x not in seen:
#             seen.add(x)
#         else:
#             non_unique.add(x)
    
    
#     unique = seen - non_unique #symetric difference

#     return non_unique, unique

# arr = [1,2,3,4,5,5,9,6,6,7,7,8,0,0,2,2,3,3]
# print(duplicate_element(arr))