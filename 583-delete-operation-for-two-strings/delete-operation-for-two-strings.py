class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = defaultdict(int)
        def dp(i, j):
            if i == len(word1) or j == len(word2):
                
                return  len(word2)  - j if i == len(word1) else len(word1)  - i
            state = (i,j)
            if state in memo:
                return memo[state]
            
            if word1[i] == word2[j]:
                memo[state] =  dp(i + 1, j + 1)
            else:
                memo[state] = min(dp(i + 1, j) + 1,dp(i, j + 1) + 1)
            return memo[state]
        return dp(0,0)