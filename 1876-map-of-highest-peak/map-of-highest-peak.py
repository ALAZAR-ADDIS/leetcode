class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        def inBound(row,col):
            return  0 <= row < len(isWater) and 0 <= col < len(isWater[0])

        ans = [ [0 for _ in range(len(isWater[0]))] for _ in range(len(isWater))]
        dirc = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()        
        qu = deque()

        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j]:
                    qu.append((i,j))
                    visited.add((i,j))
        
        
        
        level = 1
        while qu:
            leng = len(qu)
            for i in range(leng):
                row,col = qu.popleft()                
                
                for x,y in dirc :
                    r = row + x
                    c = col + y

                    if inBound(r,c) and (r,c) not in visited:
                        visited.add((r,c))
                        ans[r][c] = level
                        qu.append((r,c))
            level += 1
        return ans


            

