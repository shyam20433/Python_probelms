def two_sum(nums,target):
    d={}
    for i in range(len(nums)):
        complement=target-nums[i]
        if complement in d:
            return [d[complement],i]
        d[nums[i]]=i
    return 0

print(two_sum([2,7,8,5],9))