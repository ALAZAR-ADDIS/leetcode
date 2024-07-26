class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count={0:0,1:0}
        l=0
        maxe=0
        for i in range(len(nums)):
            count[nums[i]]+=1
            while count[0]>1:
                count[nums[l]]-=1
                l+=1

            maxe=max(count[1],maxe)
    
        if count[0]==1:
            return maxe
        elif count[0]==0:
            return maxe-1
        
        return 0
