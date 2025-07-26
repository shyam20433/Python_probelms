def longes(nums):
    count=1
    maximum=1
    for i in range(1,len(nums)):
        if nums[i]>nums[i-1]:
            count=count+1
            maximum=max(maximum,count)
        else:
            count=1
    return count 

print(longes([1,2,3,1,0,1,2,3,4]))