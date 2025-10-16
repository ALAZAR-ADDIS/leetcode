class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        def dp(i):
            if i >=  len(nums) - 1:
                return 0 if i == len(nums) - 1 else float("inf")

            if i in memo:
                return memo[i]

            minn = len(nums)
            for j in range(i + 1, i + nums[i] + 1 ):
                
                minn = min(dp(j) + 1, minn)
                if i == 1:
                    print(j,minn,i + nums[i] + 1)
            
            memo[i] = minn
            return memo[i]
        return dp(0)

            
        