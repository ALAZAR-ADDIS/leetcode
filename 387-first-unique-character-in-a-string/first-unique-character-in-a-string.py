class Solution:
    def firstUniqChar(self, s: str) -> int:
        count={}

        for i in range(len(s)):
            count[s[i]]=count.get(s[i],0)+1
        
        for index in range(len(s)):
            char=s[index]
            if count[char]==1:
                return index
        return -1
            

        
        