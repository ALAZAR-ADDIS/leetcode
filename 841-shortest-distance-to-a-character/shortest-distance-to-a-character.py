class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l=0
        prev=None
        ans=[]
        for i in range(len(s)):
            
            while s[i]==c  and l<=i:
                if prev!=None:
                    ans.append(min(l-prev,i-l))
                else:
                    ans.append(i-l)
               
                if s[l]==c:
                   prev=l
                l+=1
        while l<len(s):
            ans.append(l-prev)
            l+=1
        
            
        return ans