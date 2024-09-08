class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        newWord=""
        

        for l in s:
            if l.isalnum():
                newWord+=l
        
        l=0
        r=len(newWord)-1
        while l<r:
            if newWord[l]!=newWord[r]:
                return False
            l+=1
            r-=1
        return True
        