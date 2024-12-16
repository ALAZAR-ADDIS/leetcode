class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Sum=-float("inf")
        flag=0
        for i in range(len(nums)):
            flag+=nums[i]
            Sum=max(Sum,flag)
              
            if flag<0:
                flag=0 
            
        return Sum
            
        