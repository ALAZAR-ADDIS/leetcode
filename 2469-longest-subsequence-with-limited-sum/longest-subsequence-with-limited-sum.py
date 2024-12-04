class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans=[]
        nums.sort()
        for i in range(len(queries)):
            l=0
            total=0
            maxWind=0
            for r in range(len(nums)):
                total+=nums[r]
                while total>queries[i]:
                    total-=nums[l]
                    l+=1
                maxWind=max(maxWind,r-l+1)
            ans.append(maxWind)
        return ans
            

        