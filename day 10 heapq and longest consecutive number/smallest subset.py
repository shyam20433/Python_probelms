def smallest(nums,k):
    minimum=sum(nums[:k])
    print("minimum =",minimum)
    for i in range(1,len(nums)-k+1):
        sub=sum(nums[i:i+k])
        print("sub",sub)
        minimum=min(sub,minimum)
    return minimum


print(smallest([1,4,5,6,7,1,1,0],3))