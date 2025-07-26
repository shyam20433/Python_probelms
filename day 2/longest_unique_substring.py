def lengthOfLongestSubstring( s):
    seen=set()
    left=0
    maximum=0
    for i in range(len(s)):
        if s[i] not in seen:
            seen.add(s[i])
            maximum=max(maximum,i-left+1)
        else:
            while s[i] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[i])
    return maximum


print(lengthOfLongestSubstring("abcdeabcdefs"))

