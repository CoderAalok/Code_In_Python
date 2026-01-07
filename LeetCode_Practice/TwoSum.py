# Method-I [Time Complexity: O(n^2)]
def twosum(nums,k):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == k:
                return [i,j]
print(twosum([3,2,5,3],6))


# Method-II [Time Complexity: O(n)]
# def twosum(nums,k):
#     seen = {} 
#     for i ,val in enumerate(nums):
#         diff = k - val 
#         if diff in seen:
#             return [seen[diff],i]
#         seen[val] = i 
# print(twosum([3,3],6))