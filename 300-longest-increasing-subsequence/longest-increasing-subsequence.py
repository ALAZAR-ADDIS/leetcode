class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # memo = defaultdict(int)

        # def dp(prev):
        #     if prev == len(nums):
        #         return 0
            
        #     state = prev
        #     if state in memo:
        #         return memo[state]

        #     nottake = dp(prev + 1)
        #     take = -float("inf")
        #     for i in range(prev + 1, len(nums)):
        #         if prev == -1 or nums[i] > nums[prev]:
        #             take = max(take, dp(i) + 1)
            
        #     memo[state] = max(nottake, take)
        #     return memo[state]

        # return dp(-1)


        memo = defaultdict(int)

        def dp(i):
            if i in memo:
                return memo[i]
            memo[i] = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    memo[i] = max(dp(j) + 1 , memo[i])
            
            return memo[i]

        ans = -1
        for i in range(len(nums)):
            ans = max(dp(i),ans)
        
        return ans

