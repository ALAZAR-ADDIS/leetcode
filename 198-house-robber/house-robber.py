class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        def dp(n):
            if n in memo:
                return memo[n]
            
            if n == 0:
                return nums[0]
            
            if n < 0:
                return 0
            

            
            left = nums[n] + dp(n - 2)
            right = dp(n - 1)

            memo[n] = max(left, right) 

            return memo[n]
        return dp(len(nums) - 1)

        