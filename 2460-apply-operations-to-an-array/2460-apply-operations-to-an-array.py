class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        rightpointer=1
        leftpointer=0
        while rightpointer<len(nums):
            if nums[rightpointer]==nums[leftpointer]:
                nums[rightpointer]=0
                nums[leftpointer]=2*nums[leftpointer]
            rightpointer+=1
            leftpointer+=1  
        left=0
        for right in range(len(nums)):
            if nums[right]:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
        return nums