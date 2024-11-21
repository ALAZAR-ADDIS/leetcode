class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l=0
        r=len(skill)-1
        total=skill[0]+skill[-1]
        ans=0
        while l<r:
            if total==skill[l]+skill[r]:
                ans+=skill[l]*skill[r]
            else:
                return -1
            l+=1
            r-=1
        return ans


        