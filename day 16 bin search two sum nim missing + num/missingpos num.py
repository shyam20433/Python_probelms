def cyclic_sort(nums):
    i=0
    n=len(nums)
    while i < n:
        cur=nums[i]-1
        if 0<=cur<n and nums[i]!=nums[cur]:
            nums[i],nums[cur]=nums[cur],nums[i]
        else:
            i+=1
        print(nums)
    for i in range(n):
        if nums[i]!=i+1:
            return i+1
    return n+1

print(cyclic_sort([1,4,2,3,6,5]))