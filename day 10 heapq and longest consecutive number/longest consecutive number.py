def longest(nums):
    stack=set(nums)
    maximum=0
    for num in stack:
        if num-1 not in stack:
            count=1
            num+=1
            while num in stack:
                count+=1
                num+=1
            maximum=max(count,maximum)
    return maximum


print(longest([1,2,3,4,5,7,8,9,0,45,46,47,48,6]))