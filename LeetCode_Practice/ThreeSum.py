def threesum(nums):
    re = set()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    # re.add(tuple(sorted([nums[i] , nums[j] , nums[k]])))
                    re.add(tuple(sorted([nums[i] , nums[j] , nums[k]])))

    return [list(i) for i in re]
print(threesum([-1,0,1,2,-1,-4]))
#Too slow -> Time Complexity: O(n^3)
