class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        def dp(i,end):
            if  i >= end:
                return 0

            state = (i,end)
            if state in memo:
                return memo[state]
            
            memo[state] =  max(dp(i + 2,end) + nums[i], dp(i + 1,end))
            print(memo[state])
            return memo[state]
        if len(nums) == 1:
            return nums[0]
        return max(dp(0, len(nums) - 1),dp(1, len(nums)))