
s ="Shyam1234"
upper = []
lower = []
even = []
odd = []
for i in sorted(s):
    if i.isupper():
        upper.append(i)
    elif i.islower():
        lower.append(i)
    
    elif int(i)%2==0:
        even.append(i)
    else:
        odd.append(i)
string1 = lower + upper
string2 = odd + even
string3 = string1 + string2
print("".join(string3))




