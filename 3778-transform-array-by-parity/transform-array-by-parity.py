class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for index,num in enumerate(nums):
            nums[index] = 1 if num % 2 else 0
        nums.sort()
        return nums
        