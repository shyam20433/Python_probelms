def climbstair(n):
    if n ==1:
        return 1
    elif n==2:
        return 2
    a=1
    b=2
    for i in range(2,n):
        current=a+b
        a=b
        b=current
    return b


print(climbstair(5))