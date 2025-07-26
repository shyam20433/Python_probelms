def operation(a,b,i):
    if i=="-":
        return f"{b} - {a}"
    elif i=="+":
        return f"{b} + {a}"
    elif i=="*":
        return f"{b} * {a}"
    elif i=="^":
        return f"{b} ^ {a}"
    elif i=="/":
        return f"{b} / {a}"
    elif i=="%":
        return f"{b} % {a}"
    
def expression(equation):
    stack=[]
    for i in equation:
        if i.isalpha():
            stack.append(i)
        else:
            a=stack.pop()
            b=stack.pop()
            c=operation(a,b,i)
            stack.append(c)
    
    return stack
    
print(expression("ab-cd+*ef+-"))