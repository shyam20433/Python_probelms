def paranthesis(s):
    stack=[]
    brackets={"]":"[","}":"{",")":"("}

    for character in s:
        if character  in brackets:
            top=stack.pop()
            if top!=brackets[character]:
                return False
        else:
            stack.append(character)
    return True

print(paranthesis("[{}]"))