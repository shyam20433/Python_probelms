def maximum(nums):
    max=nums[0]
    for i in nums:
        if i>max:
            max=i
    return max


print(maximum([1,2,3,9,4,3,2]))