# # Searching for pick value from a array  [Linner scan:check every elements Vs neighbours] 
# class Solution:
#     def pick_element(self,arr):
#         if not arr:
#             return None
#         pickValue = arr[0] #[arr[0]] # First hold 0th index value later it will change if greater than it's
#         index_pick = 0
#         for i in range(1,len(arr)):
#            if arr[i] > arr[i-1] and arr[i] > pickValue:
#                 pickValue = arr[i]
#                 index_pick = i
#             #    if arr[i] > pickValue[0]:
#             #         pickValue[0] = arr[i]
#             #         index_pick = i
#         return pickValue,index_pick
# # [Time Complexity: O(n)]
# # [Axulliary Space: O(1)]

# arr = [1,5,3,7,0,3]
# soln = Solution()
# print(soln.pick_element(arr))

# Find target index in sorted array using Binary Search Logic
# def sortt(arr,target):
#     low = 0
#     high = len(arr)-1
#     while low <high:
#         mid = (low+high)//2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target: #Right move
#             low = mid+1
#         elif arr[mid] > target: #left move
#             high = mid-1
#     return arr[high]

# arr = [2,3,5,7,9]
# target = 7
# print(sortt(arr,target))

# Find PickValue from an array using Binary Search
def pickValue(arr):
    if not arr:
        return None
    low = 0 #start
    high = len(arr)-1 # end
    while low < high:
        mid = (low+high)//2
        if arr[mid] > arr[mid+1]:
            high = mid #forward moves
        else:
            low = mid+1  #backward moves
    return high , arr[high]
print(pickValue([2,3,5,6,8,2]))
# Time Complexity: O(logn)
# Axulliary Space: O(1)