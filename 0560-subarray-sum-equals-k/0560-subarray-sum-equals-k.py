class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count={0:1}
        c,prefixSum=0,0
        for r in range(len(nums)):
            prefixSum+=nums[r]
                        
            c+=count.get(prefixSum-k,0)

            count[prefixSum]=count.get(prefixSum,0)+1

        return c
       
            
        