class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            for r in range(1, target + 1):
                sqr = r * r
                if target - sqr < 0 :
                    break
                
                dp[target] = min(dp[target], 1 + dp[target - sqr])
            
        return dp[n]
        
       