def reverse(nums):
    front=0
    rear=len(nums)-1

    while front<rear:
        nums[front],nums[rear]=nums[rear],nums[front]
        front+=1
        rear-=1
    return nums

print(reverse([1,2,3,4,5,6]))