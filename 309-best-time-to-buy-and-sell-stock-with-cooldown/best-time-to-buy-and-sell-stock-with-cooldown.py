class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # options at the ith day are -> buy
        #                            -> sale the sale to the  next day
        #                            -> sale and  buy the stock after 1 day
        memo = defaultdict(int)
        def dp(i, state):
            if i >= len(prices):
                return 0
            
            if (i, state) in memo:
                return memo[(i, state)]

            cooldown = dp(i + 1 , state)
            if state:
                buy = dp(i + 1, not state) - prices[i]
                memo[(i, state)] = max(buy, cooldown)
                
            else:
                sale = dp(i + 2, not state) + prices[i]
                memo[(i, state)] =  max(sale, cooldown)
            return memo[(i, state)]
        
        return dp(0, True)
        
            