def return_count_1(nums):
    count={}

    for i in nums:
        count[i]=count.get(i,0)+1

    for i in nums:
        if count[i]==1:
            return i

    return -1
print(return_count_1([1,2,3,1]))