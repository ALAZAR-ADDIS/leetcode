class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        l = 0

        while l < len(nums):
            corr = nums[l] -1
            if nums[corr] == nums[l]:
                l += 1
            else:
                nums[l],nums[corr] = nums[corr],nums[l]
        ans = []


        
        
        for i in  range(len(nums)):
            if  i + 1 != nums[i]:
                ans.append(i + 1)
        return ans

        