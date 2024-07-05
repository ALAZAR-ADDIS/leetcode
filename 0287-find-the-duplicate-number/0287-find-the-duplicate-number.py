class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        index=0
        while index<len(nums):
            correct=nums[index]-1
            if nums[index]!=nums[correct]:
                nums[index],nums[correct]=nums[correct],nums[index]
            else:
                if index!=correct and nums[index]==nums[correct]:
                    return nums[correct]
                index+=1
       
        