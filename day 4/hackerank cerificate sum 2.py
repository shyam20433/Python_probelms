def trnasformation(sentence):
    words=sentence.split()
    result=[]
    for word in words:
        trans=word[0]

        for i in range(1,len(word)):
            prev=word[i-1].lower()
            current=word[i].lower()

            if prev<=current:
                trans+=current.upper()
            elif prev < current:
                trans+=current.lower()
            else:
                trans+=current
        result.append(trans)
    return ' '.join(result)

print(trnasformation("Abcde abcd"))