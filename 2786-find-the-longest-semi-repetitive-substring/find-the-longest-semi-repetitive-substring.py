class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        count=0
        l=0
        maxl=0
        for i in range(len(s)):
            if i>0 and s[i-1]==s[i]:
                count+=1
            while l+1<i and count>1:
                if s[l]==s[l+1]:
                    count-=1
                l+=1
            maxl=max(maxl,i-l+1)
        return maxl
            
        