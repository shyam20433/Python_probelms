def first_repeat(nums):
    count={}
    for i in nums:
        count[i]=count.get(i,0)+1

    for i in nums:
        if count[i]==2:
            return i
     
    return -1
print(first_repeat([1,2,3,3,2]))