def min_sum(nums,k):
    if len(nums)<k:
        return -1
    mini=0
    min_sum=sum(nums[:k])
    low=min_sum
    for i in range(k,len(nums)-k+1):
    #for i in range(k,len(nums)):
       # min_sum+=nums[i]-nums[i-k]
        mini=sum(nums[i:i+k])
        #print(mini)
        low=min(low,mini)
    return f" min is {low}"


print(min_sum([1,2,1,1,1,1,6],2))
