class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        dirc = [(-1,0),(0,-1),(0,1),(1,0)]
        visited = set()
        def isBounde(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        def dfs(i,j):
            visited.add((i,j))
            grid[i][j] = 0

            for x,y in dirc:
                row = x + i
                col = y + j
                if isBounde(row, col) and (row,col)not in visited and grid[row][col]:
                    dfs(row,col)
        
        for i in range(len(grid)):
            if grid[i][0]:
                dfs(i,0)
            if grid[i][len(grid[0]) - 1]:
                dfs(i, len(grid[0]) - 1)
        for i in range(len(grid[0])):
            if grid[0][i]:
                dfs(0,i)
            if grid[len(grid) - 1][i]:
                dfs(len(grid) - 1, i)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    ans += 1
        return ans

        