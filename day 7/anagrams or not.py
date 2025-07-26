def anagram(a,b):
    a=list(a)
    b=list(b)
    if sorted(a)==sorted(b):
        return True
    return False
print(anagram("shyam","syhma"))