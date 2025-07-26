def happy_numbers(num):
    seen=set()
    current=str(num)

    while current not in seen:
        seen.add(current)
        total=0
        for i in current:
            total+=int(i)**2
        if total==1: return True

        current=str(total)

    return False


print(happy_numbers(19))