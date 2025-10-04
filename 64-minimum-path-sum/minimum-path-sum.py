class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = defaultdict(int)
        def dp(i, j):
            if i >= len(grid) or j >= len(grid[0]):
                return float("inf")
            
            if (i,j) in memo:
                return memo[(i,j)]
            minn = min( dp(i  + 1, j ), dp(i , j + 1) )
            
            memo[(i,j)] = (minn if minn != float("inf") else 0) + grid[i][j]
            return memo[(i,j)]
        return dp(0,0)
            

        