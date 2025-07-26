def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if target-nums[i]==nums[j]:
                return f"{i},{j}"
    return -1

print(two_sum([1,2,3,4,5,6],11))