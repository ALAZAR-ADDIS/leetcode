class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirc = [(0,1),(1,0),(0,-1),(-1,0)]
        def inBound(i,j):
            return 0 <= i < len(board) and 0 <= j < len(board[0])

        def dfs(pos,k):
            if k == len(word):
                return True
            visited.add(pos)
            i,j = pos

            for x,y in dirc:
                row = x + i
                col = y + j
                
                if inBound(row,col) and (row,col) not in visited and board[row][col] == word[k]:
                    if dfs((row,col), k + 1):
                        return True
                    else:
                        visited.remove((row,col))
       

            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                if board[i][j] == word[0]:
                    if dfs((i,j),1):
                        return True
                    print(visited,"done")
                   
        return False


        