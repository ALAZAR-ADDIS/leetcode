class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        l=0 
        window=0
        count=0
        for r in range(len(nums)):
            if left<=nums[r]<=right:
                window=r-l+1
            elif nums[r]>right:
                window=0
                l=r+1
            count+=window
        return count
            
        
        
            
            
