class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_val = -float("inf")
        run = 0
        for i in range(len(nums)):
            run += nums[i]
            max_val = max(max_val , run)

            if run < 0 :
                run = 0
        return max_val
        