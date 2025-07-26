def power(x,n):
    ans=1
    num=n
    if n<0:
        num=-1*n
    while num!=0:
        if num%2==0:
            x=x*x
            num=num//2
        else:
            ans=ans*x
            num=num-1
    if n<0:
        return 1/ans
    return ans

print(power(2,3))