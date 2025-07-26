def intersection(nums1,nums2):
    '''result=[]
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            result.append(nums1[i])
    return result'''

    print( list(set(nums1)&set(nums2)) )#return  intersection value
    return  ( list(set(nums1) | set(nums2)) ) # return union values
    


print(intersection([1,2,3,4,5,6],[4,7,3]))