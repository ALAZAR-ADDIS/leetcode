class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while r>l:
            if s[r]!=s[l]:
                skipl,skipr=s[l+1:r+1],s[l:r]
                return (skipl==skipl[::-1] or skipr==skipr[::-1])
            l+=1
            r-=1
        return True
        
        