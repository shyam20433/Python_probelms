def count(nums):
    k=0
    for i in nums:
        if i%2==0:
            nums[k]=i
            k=k+1
    return nums[:k] 
a=[5,6,7,8,9]
print(count(a))