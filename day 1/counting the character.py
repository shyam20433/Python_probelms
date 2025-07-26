def counting(nums,target):
    count=0
    for i in range(len(nums)):
        if nums[i]==target:
            count+=1
    return count


print(counting([1,2,3,1,2,1,6],1))