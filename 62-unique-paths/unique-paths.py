class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = defaultdict(int)
        def dp(i, j):
            print(i,j)
        
            if i == m - 1 and j == n -1:
                return 1

            if i >= m or j >= n:
                return 0
                
            if (i,j) in memo:
                    return memo[(i,j)]          
               
           
            memo[(i,j)] += dp(i, j + 1) + dp(i + 1, j)
            return memo[(i,j)]
        return dp(0,0)
        