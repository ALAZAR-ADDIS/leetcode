class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        l = 0
        r = len(nums) - 1
        minn = float("inf")
        while l < r:
            minn = min(minn,(nums[l] + nums[r])/2)
            l += 1
            r -= 1
        return minn
        
        