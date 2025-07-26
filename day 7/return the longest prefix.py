'''def prefix(lists):
    if not lists:
        return ""
    prefix=lists[0]

    for i in lists[1:]:
        while not i.startswith(prefix):
            print(prefix)
            prefix=prefix[:-1]
            if not prefix:
                return ""
    return prefix


print(prefix(["flower","flower","floight"]))'''

a=["flower","flowers","flowght"]

prefix=a[0]

for i in a:
    while prefix not in i[:(len(prefix))]:
        prefix=prefix[:-1]
        if not prefix:
            print("")
print( prefix)
        
