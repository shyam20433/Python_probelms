a=[1,3,5]
b=[2,4,6]
def merge(a,b):
    i=0
    j=0
    
    sort=[]
    while i< len(a) and j < len(b):
        if a[i]<b[j]:
            sort.append(a[i])
            i+=1
        else:
            sort.append(b[j])
            j+=1
        
    while i < len(a):
        sort.append(a[i])
        i += 1

    while j < len(b):
        sort.append(b[j])
        j += 1
    return sort

print(merge(a,b))