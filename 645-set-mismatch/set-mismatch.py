class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        l = 0

        while l < len(nums):
            corr  = nums[l] - 1
            if nums[corr] == nums[l]:
                l += 1
            else:
                nums[corr],nums[l] = nums[l] , nums[corr]
        
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return [nums[i], i + 1]