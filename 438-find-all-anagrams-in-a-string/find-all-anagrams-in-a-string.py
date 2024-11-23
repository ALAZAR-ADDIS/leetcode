class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
            
            if len(p)>len(s):
                return []
            ans=[]
            target={}
            count={}
                            
            for j in range(len(p)):
                target[p[j]]=target.get(p[j],0)+1
                count[s[j]]=count.get(s[j],0)+1
            if count==target:
                ans.append(0)
            for i in range(len(s)-len(p)):
                
                count[s[i+len(p)]]=count.get(s[i+len(p)],0)+1
                count[s[i]]-=1
                if count[s[i]]==0:
                    count.pop(s[i])

                if count==target:
                    ans.append(i+1)
            
            return ans
            

