class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #return the number which is duplicated
        #cycle sort

        #sortin algorithm 
        index=0
        while index<len(nums):
            correct=nums[index]
            if correct<len(nums) and nums[index]!=nums[correct]:
                nums[index],nums[correct]=nums[correct],nums[index]
            else:
                index+=1

        #find the duplicates
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        return len(nums)

      