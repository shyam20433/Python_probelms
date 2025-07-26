def quick_sort(nums):
    if len(nums)<=1:
        return nums
    else:
        pivot=nums[-1]
        i=[x for x in nums[:-1] if x<pivot]
        k=[x for x in nums[:-1] if x>= pivot]
        return quick_sort(i) + [pivot] + quick_sort(k)
print(quick_sort([4,2,7,9,5,8,1,3,6]))