class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = defaultdict(int)
        def dp(i,j): 
            #moving dowm (i + 1, j) ,moving up (i, j + 1)
            if j == len(obstacleGrid[0]) - 1 and i == len(obstacleGrid) - 1  :
                
                return 1 if obstacleGrid[i][j] == 0 else 0
            if j == len(obstacleGrid[0]) or i == len(obstacleGrid):
                return 0
            state = (i,j)
            if state in memo:
                return memo[state]
           
            if obstacleGrid[i][j] == 0:
                memo[state] = dp(i + 1, j) + dp(i, j + 1)
            

            return memo[state]
        
        return dp(0,0)

        