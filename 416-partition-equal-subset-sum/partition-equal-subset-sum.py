class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = defaultdict(bool)
        def dp(n,total):
            if total == 0:
                return True

            if n == 0 :
                return nums[0] == total

            if total < 0:
                return False

            state = (n, total)
            if state in memo :
                return memo[state]
            
            memo[state] = dp(n - 1,total - nums[n]) or dp(n- 1, total)

            return memo[state]
        

        

        
        target = sum(nums)
        if target % 2:
            return False

        return dp(len(nums) - 1, target//2)
            
    