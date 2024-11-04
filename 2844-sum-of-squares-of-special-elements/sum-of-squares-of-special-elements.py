class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        l=len(nums)
        total=0
        for i in range(len(nums)):
            if l%(i+1)==0:
                total+=nums[i]**2
        return total


        