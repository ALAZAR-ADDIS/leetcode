class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = defaultdict(int)
        def dp(i, state):
            if i == len(prices):
                return 0
            s = (i,state)
            if s in memo:
                return memo[s]
            if state:
                memo[s] =  max(dp(i + 1,not state) - prices[i], dp(i + 1, state))
            else:
                memo[s] = max(dp(i + 1,not state) + prices[i], dp(i + 1,  state))
                
            return memo[s]
        return dp(0,True)
            

        