class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        sum_num = 0
        sum_xor = 0
        ans = 1
        for r in range(len(nums)):
            sum_num += nums[r]
            sum_xor ^= nums[r]
            while sum_num != sum_xor:
                sum_num-= nums[l]
                sum_xor ^= nums[l]
                l += 1
            ans = max(ans, r - l + 1)
        return ans
            


       