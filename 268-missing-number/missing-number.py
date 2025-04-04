class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # nums.sort()        
        # for i in range(len(nums)):
        #     if i< len(nums) and nums[i]!=i:
        #         return i
        # return len(nums)


        l = 0
        while l < len(nums):
            corr = nums[l]
            if corr >= len(nums) or nums[corr] == nums[l]:
                l += 1
            else:
                nums[corr],nums[l] = nums[l], nums[corr]
        for i in range(len(nums)):
            if i != nums[i]:
                return i 
        return len(nums)

        
        