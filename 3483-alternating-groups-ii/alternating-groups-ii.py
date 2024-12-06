class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

        alt=0
        for i in range(k-1):
            if colors[i]!=colors[i+1]:
                alt+=1
        ans=1 if alt==k-1 else 0
        l=0
        r=k-1
        while l<len(colors)-1:
            if colors[l]!=colors[l+1]:
                alt-=1
            if colors[r%len(colors)]!=colors[(r+1)%len(colors)]:
                alt+=1
            ans+=1 if alt==k-1 else 0
            l+=1
            r+=1
        return ans


    
    
        