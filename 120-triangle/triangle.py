class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # memo = [[- 1] * (i + 1) for i in range(len(triangle))]
        memo = defaultdict(int)
       
        def dp(i,j):
            state = (i,j)
            if i >= len(triangle):
                return 0

            if state in memo :
                return memo[state]
            
            memo[state] = min(dp(i + 1,j),dp(i + 1, j + 1)) + triangle[i][j]
            return memo[state]
        
        return dp(0,0)
        