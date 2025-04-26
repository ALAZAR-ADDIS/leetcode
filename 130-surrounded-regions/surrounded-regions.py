class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.        """
        def dfs(row , col):
            visited.add((row,col))
            res = True
            

            for x,y in dirc:
                r = row + x
                c = col + y
                if inbound(r,c):
                    if (r,c) not in visited and board[r][c] == "O":
                        if not  dfs(r,c):
                            res = False
                else:
                    res = False
                        
                          
    
            return res
        
        def fill(row , col):
            visited2.add((row,col))
            
            for x,y in dirc:
                r = row + x
                c = col + y
                if inbound(r,c):
                    if (r,c) not in visited2 and board[r][c] == "O":
                        fill(r,c)
            
                board[row][col] = "X"
                                

           
                       
            return True

        dirc = [(-1,0),(0,-1),(1,0),(0,1)]
        visited = set()
        visited2 = set()

        def inbound(row,col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if (i,j) not in visited and board[i][j] == "O":
                    print(i,j,"is called")  
                    res = dfs(i,j)
                    print(res)
                                  
                    
                     
                    if res :
                        fill(i,j)
                                   
        
        
        return board


        