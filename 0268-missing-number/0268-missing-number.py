class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        index=0
        while index<len(nums):
            correct=nums[index]
            if correct<len(nums) and nums[correct]!=nums[index]   :
                 nums[correct],nums[index]=nums[index],nums[correct]
            else:
                index+=1
               
        count=0
        while count<len(nums):
            if nums[count]!=count:
                return count
            count+=1
        return len(nums)
        
       
        