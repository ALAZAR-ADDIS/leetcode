class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans=0
        l,r=0,0
        while l<len(s) and r<len(g):
            while l<len(s) and  s[l]<g[r]:
                print(s[l],g[r])
                l+=1
            if l>=len(s):
                break
            ans+=1

            r+=1
            l+=1
        return ans


            
        