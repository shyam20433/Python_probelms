def remove_duplicates(nums):
    k=0
    for i in range(len(nums)):
        if nums[k]!=nums[i]:
            print(nums)
            k+=1
            nums[k]=nums[i]
    return nums[:k+1],k

print(remove_duplicates([0,0,1,1,2,2]))