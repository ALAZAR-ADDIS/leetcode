class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        index=0
        while index<len(nums):
            correct=nums[index]-1
            if correct<len(nums) and correct>-1 and   nums[index]!=nums[correct]:
                nums[correct],nums[index]=nums[index],nums[correct]
            else:
                index+=1
    
        for i in range(len(nums)):
            if nums[i]-1!=i:
                return i+1
           
        return len(nums)+1

        