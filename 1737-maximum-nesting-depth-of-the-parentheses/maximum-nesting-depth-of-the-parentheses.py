class Solution:
    def maxDepth(self, s: str) -> int:

        Debth_count=0
        Debth=0

        for i in range(len(s)):
            if s[i]=="(":
                Debth+=1
            elif s[i]==")":
                Debth-=1
            Debth_count=max(Debth_count,Debth)
                
           
        return Debth_count
        