class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l=0
        r=len(people)-1
        ans=0
        people.sort()
        while l<=r:
                
                total=people[l]+people[r]
                if total<=limit:
                   l+=1
                   r-=1
                else:
                    r-=1
                ans+=1
        return ans
            
            
           

