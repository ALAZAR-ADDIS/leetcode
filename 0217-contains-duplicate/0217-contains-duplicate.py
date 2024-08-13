class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        l=0
        r=1
        while r<len(nums):
            if nums[l]==nums[r]:
                return True
            r+=1
            l+=1

        