def target_index(nums,target):
    
    if target in nums:
        for i in range(len(nums)):
            if target==nums[i]:
                return i
    else:
        return -1
        

    return 

print(target_index([1,2,3,4,5],3))