def fibonanci(n):
    if n ==0:
        return 0
    elif n==1:
        return 1
    a=0
    b=1
    for i in range(n):
        current=a+b
        a=b
        b=current
    return a


print(fibonanci(9))
