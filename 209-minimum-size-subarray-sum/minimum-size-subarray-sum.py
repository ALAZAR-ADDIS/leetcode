class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l=0
        sum=0
        size=float("inf")
        for r in range(len(nums)):
            sum+=nums[r]
            while sum>=target:
                size=min(size,r-l+1)
                sum-=nums[l]
                l+=1
            
        return 0 if l==0 else size

                   

        