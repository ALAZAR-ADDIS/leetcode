class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        dirc = [(-1,0),(0,-1), (1,0), (0,1)]
        visited = set()

        def inBound(row, col):
            return 0 <= row < len(grid) and  0 <= col < len(grid[0])
        
        def dfs(i,j,char,prev):
            visited.add((i,j))

            for x,y in dirc:
                row = x + i
                col = y + j
                if inBound(row,col) and grid[row][col] == char:
                    if (row,col) not in visited:
                        if dfs(row,col,char,(i,j)):
                            return True
                    elif prev != (row,col) :
                      return True
                        
            
            return False
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited:
                    print(i,j)
                    if dfs(i,j,grid[i][j],(-1,-1)):
                        return True
        return False

        