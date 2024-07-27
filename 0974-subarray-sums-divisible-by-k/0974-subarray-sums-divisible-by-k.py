class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count={0:1}
        c,prifixSum=0,0
        for r in range(len(nums)):
            prifixSum+=nums[r]
                            
            value=prifixSum%k
            c+=count.get(value,0)

            count[value]=count.get(value,0)+1 
        return c

         
