def armstrong(num):
    total=0
    current=num
    n=len(str(num))
    for i in str(num):
        total+=int(i)**n
    if num==total:
        return True
    
    return False
        
print(armstrong(153))