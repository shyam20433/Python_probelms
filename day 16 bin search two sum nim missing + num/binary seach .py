def bin_search(nums,target):
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2

        if nums[mid]==target:
            return f"{target} found at index {mid}"
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return False

print(bin_search([10,20,30,40,50,60],60))