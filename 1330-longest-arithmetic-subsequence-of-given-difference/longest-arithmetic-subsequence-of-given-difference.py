class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        memo = defaultdict(int)

        # def dp(i,prev):
        #     if i == len(arr):
        #         return 0

        #     state = (i,prev)
        #     if  state in memo:
        #         return memo[state]
            
        #     memo[state] = dp(i + 1, prev)
        #     if prev < 0 or arr[i] - arr[prev] == difference:                
        #         memo[state] = max(memo[state], dp(i + 1, i) + 1)           
            
        #     return memo[state]
        
        # return dp(0,-1)

        dp = defaultdict(int)


        for i in range(len(arr)- 1, -1, -1):
            if arr[i]  in dp:
                dp[arr[i] - diff] = dp[arr[i]]  + 1
            else:
                dp[arr[i] - diff] = 1
        return max(dp.values())
            
            
    
        


            

            

        