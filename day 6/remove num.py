def remove(nums,vals):
    k=0
    for i in range(len(nums)):
        
        if nums[i]!=vals:
            nums[k]=nums[i]
            print(nums)
            k+=1
    return nums[:k]


print(remove([0, 1, 2, 2, 3, 0, 4, 2],2))