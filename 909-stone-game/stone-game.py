class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = defaultdict(bool)
        # def dp(i,j , summ):
        #     if i > j:
        #         return sum(piles) - summ < summ
            
        #     state = (i,j, summ)
        #     if state in memo:
        #         return memo[state]
            
        #     memo[state] =  dp(i + 2,j, summ + piles[i]) or dp(i, j - 2,summ + piles[j])
        #     return memo[state]
        
        # return dp(0, len(piles) - 1,0)

        def dp(i,j):
            if i > j:
                return 0

            state = (i,j)
            if state in memo:
                return memo[state]
            
            left = piles[i] if (j - i + 1) % 2 == 0 else 0
            right = piles[j] if (j - i + 1) % 2 == 0 else 0

            memo[state] = max(dp(i + 1,j) + left, dp(i, j -1) + right)
            return memo[state]
        
        maxx = dp(0, len(piles) - 1)
        return sum(piles) - maxx < maxx

      
        