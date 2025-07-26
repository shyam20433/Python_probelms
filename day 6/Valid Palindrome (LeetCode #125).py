class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        s=s.replace(",","").replace(" ","")
        # or use regular expression 
        # s = re.sub(r'[^a-z0-9]', '', s)   re.sub(punctuations,replace with , string)
        i=0
        j=len(s)-1

        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True


            
        
print(Solution().isPalindrome("malayalam"))