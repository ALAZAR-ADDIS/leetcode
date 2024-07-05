class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        index=0
        while index<len(nums):
            correct=nums[index]
            if correct==index or  correct>=len(nums):
                index+=1
            else:
                nums[correct],nums[index]=nums[index],nums[correct]
        count=0
        while count<len(nums):
            if nums[count]!=count:
                return count
            count+=1
        return len(nums)
        
       
        