class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        qu = deque()
        dirc = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        def inBound(row,col):
            return  0 <= row < len(grid) and 0 <= col < len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    qu.append((i,j))
                    visited.add((i,j))
                    
        if not fresh:
            return 0
        time = -1
        curr = 0

     

        while qu:
            leng = len(qu)
            for _ in range(leng):
                row,col = qu.popleft()
                

                for x,y in dirc:
                    r = row + x
                    c = col + y
                    if inBound(r,c) and (r,c) not in visited and grid[r][c] == 1:
                        visited.add((r,c))
                        curr += 1
                        qu.append((r,c))
            time += 1
        
        return time if curr == fresh else -1

        

        