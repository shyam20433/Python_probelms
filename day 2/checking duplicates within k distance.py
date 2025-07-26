def check_duplicates(nums,k):
    set=[]
    for i in range(len(nums)):
        if nums[i] in set:
            return True
        
        set.append(nums[i])
        if i >=k:
            set.pop(i-k)
        print(set)

    return False


print(check_duplicates([1,2,3,6,1],4))