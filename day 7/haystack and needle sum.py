def substr(haystack,needle):
    if not needle:
        return 0
    
    for i in range(len(haystack)):
        if haystack[i:(i + len(needle))]==needle:
            return i
    return -1

print(substr("shyamsundar","ms"))