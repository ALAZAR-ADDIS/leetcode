class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

       

       

        def solve(row,col):          
            count = 0
            visited[row][col] = True
            for x,y in dirc:
                r = row + x
                c = col + y
                if check(r,c) and  grid[r][c] :                    
                    if not visited[r][c]:                                       
                        count += solve(r,c)
                else:
                 
                    count += 1
            return count

        
        dirc = [(1,0),(0,1),(-1,0),(0,-1)]
        def check(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        visited = [[False for  _ in range(len(grid[0]))] for _ in range(len(grid))]

        for  i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return solve(i,j)
        


            
        