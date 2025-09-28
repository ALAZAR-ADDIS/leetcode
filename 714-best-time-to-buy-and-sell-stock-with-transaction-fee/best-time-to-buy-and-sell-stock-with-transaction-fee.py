class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = defaultdict(int)
        def dp(i, state):
            if i >= len(prices):
                return 0
            
            if (i, state) in memo:
                return memo[(i, state)]
            cooldown = dp(i + 1, state)
            if state:
                buy = dp(i + 1, not state) - fee - prices[i]
                memo[(i, state)] = max(cooldown, buy)
            else:
                sale =  dp(i + 1, not state) +  prices[i]
                memo[(i, state)] = max(cooldown, sale)
            return memo[(i, state)]
        
        return dp(0, True)

        