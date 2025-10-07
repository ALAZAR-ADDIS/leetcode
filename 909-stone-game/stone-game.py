class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = defaultdict(bool)
        def dp(i,j , summ):
            if i > j:
                return sum(piles) - summ < summ
            
            state = (i,j, summ)
            if state in memo:
                return memo[state]
            
            memo[state] =  dp(i + 2,j, summ + piles[i]) or dp(i, j - 2,summ + piles[j])
            return memo[state]
        
        return dp(0, len(piles) - 1,0)

      
        