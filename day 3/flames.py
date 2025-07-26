
'''
f=["","","","m","",""]

def flames(f,stack):
    if len(f)==1:
        print(f"relationship between {name1} and {name2} is {f[0]}",) 
    elif len(stack)%len(f)==0:
        f.pop(-1)
        flames(f,stack)
    else:
        l=len(stack)%len(f)
        f.pop(l-1)
        flames(f,stack)
    return "completed"

def flames_calculator(name1,name2):
    stack=[]
    stack2=[]
    
    for i in range(len(name1)):
        stack.append(name1[i])
    
    for i in name2:
        if i in stack:
            stack.remove(i)
        else:
            stack2.append(i)
    for i in stack2:
        stack.append(i)
    return stack
    
while(True):
    name1=str(input("enter the name "))
    name2=str(input("enter the name "))
    new_stack=flames_calculator(name1,name2)
    print(new_stack)
    print(flames(f,new_stack))
'''
def flames(f, stack, name1, name2, index=0):
    if len(f) == 1:
        print(f"Relationship between {name1} and {name2} is {f[0]}")
        return "Completed"
    
    l = len(stack) % len(f)  
    if l == 0:
        l = len(f)
    
    index = (index + l - 1) % len(f)  
    print(f"Removing: {f[index]} at index {index}")
    f.pop(index)  

    
    return flames(f, stack, name1, name2, index)

def flames_calculator(name1, name2):
    stack = list(name1)
    stack2 = []

    for i in name2:
        if i in stack:
            stack.remove(i)
        else:
            stack2.append(i)
    
    return stack + stack2  

while True:
    name1 = input("Enter the first name: ").strip().lower()
    name2 = input("Enter the second name: ").strip().lower()
    
    new_stack = flames_calculator(name1, name2)
    print("Final Stack:", new_stack)
    
    
    print(flames(["f", "l", "a", "m", "e", "s"], new_stack, name1, name2))
