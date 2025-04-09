class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(row,col):           
            visited.add((row,col))          

            for x,y in dire:
                r = row + x
                c = col +  y
                if check(r, c) and (r,c) not in visited and grid[r][c] == "1":                 
                    dfs(r,c)
            
        def check(row , col):
            return 0 <= row < len(grid) and  0 <= col < len(grid[0])
        visited = set()
        dire = [(1,0), (-1,0), (0,1), (0,-1)] 
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j)  not in visited and grid[i][j]== "1":
                    print(i,j)
                    ans += 1
                    dfs(i,j)
        return ans