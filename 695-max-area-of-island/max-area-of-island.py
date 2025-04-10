class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(row,col):

            visited.add((row,col))
            count = 0
            for x,y in dire:
                r = row + x
                c = col + y
                if inBound(r, c) and (r,c) not in visited and grid[r][c]:
                    count += 1 + dfs(r,c)
           
            return count


        def inBound( row, col):
            return 0<= row < len(grid) and 0 <= col < len(grid[0])

        dire = [(0,-1),(-1,0),(1,0),(0,1)]
        visited = set()
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j]:
                    val = dfs(i,j)
                   
                    ans = max(ans, val + 1)
        return ans
        