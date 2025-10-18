class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = defaultdict(int)
        def dp(i,state,tran):
            if i == len(prices) :
                return 0

            s = (i,state,tran)
            if s in memo:
                return memo[s]

            if state:
                if tran >= 2:
                    memo[s] = 0
                    return memo[s]                
             
                memo[s] =  max(dp(i + 1,not state, tran + 1) - prices[i], dp(i + 1, state, tran))
            else:
                memo[s] =  max(dp(i + 1,not state, tran )  +  prices[i], dp(i + 1, state, tran))
            return memo[s]
        return dp(0, True, 0)
        