class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l=0
        count={}
        ans=0
        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0)+1
            while len(count)>3 or count.get(s[r],0)>1:
                count[s[l]]-=1
                if count[s[l]]==0:
                    count.pop(s[l])
                l+=1
            if r-l+1==3:
                ans+=1
        return ans




        