class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:


        qu = deque()
        ans = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        visited = set()
        level = 1
        dirc = [(-1,0),(0,-1),(0,1),(1,0)]

        def inBound(row,col):
            return 0 <= row < len(mat) and 0 <= col < len( mat[0] )


        for i  in range(len(mat)):
            for j in range(len(mat[0])):
                if not mat[i][j]:
                    qu.append((i,j))
                    visited.add((i,j))
        
        while qu:
            leng = len(qu)
            for _ in range(leng):
                row, col = qu.popleft()
                for x,y in dirc:
                    r = row  + x
                    c = col + y
                    if inBound(r,c) and (r,c) not in visited:
                        qu.append((r,c))
                        ans[r][c] = level
                        visited.add((r, c))
            level += 1

        return ans
