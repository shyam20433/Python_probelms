def move_zeros(nums,val):
    k=0
    for i in range(len(nums)):
        if nums[i]!=val:
            nums[k]=nums[i]
            k+=1
    return nums[:k]
    
print(move_zeros([1,0,3,0,2],0))