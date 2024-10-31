class Solution:
     def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Dict={}
        s2Dict={}
        l=0
        for i in range(len(s1)):
            s1Dict[s1[i]]=s1Dict.get(s1[i],0)+1
        
        for r in range(len(s2)):
            s2Dict[s2[r]]=s2Dict.get(s2[r],0)+1
            window=r-l+1
            if window>len(s1):
                if s2Dict[s2[l]]==1:
                    s2Dict.pop(s2[l])
                else :
                    s2Dict[s2[l]]-=1
                l+=1
            
            if s2Dict==s1Dict:
                return True
        return False
                