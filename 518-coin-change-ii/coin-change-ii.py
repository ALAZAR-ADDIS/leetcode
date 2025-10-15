class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = defaultdict(int)
        def dp(i,total):
            if total == 0:
                return 1
            if total < 0 or i == len(coins):
                return 0
            state = (i, total)
            if state in memo:
                return memo[state]
            
            memo[state] =  dp(i , total - coins[i]) + dp(i + 1, total)
            return memo[state]
        return dp(0,amount)
        