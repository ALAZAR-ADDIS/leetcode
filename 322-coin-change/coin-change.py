class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = defaultdict(int)

        def dp(i,c):
            state = (i,c)
            if state in memo:
                return memo[state]
            if c == 0:
                return 0

            if i < 0:
                return float("inf")
                

            times = 0
            minn =  dp(i - 1, c)
            if c >= coins[i]:
               
                val  = dp(i ,c - coins[i])
                
                minn = min(minn, val  + 1)
               
            memo[state] = minn

            return minn
        val = dp(len(coins) - 1, amount)
        return val  if val != float("inf")  else -1
        

            

        