class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for j in range(len(board[0])):
            num_count = Counter()          
            
            for i in range(len(board)):

                num_count[board[i][j]] += 1 if board[i][j] != "." else 0 
                if num_count[board[i][j]] >1:                                      
                            return False              
                                
                if  i%3 == 0 and j %3 ==0:

                    in_count = Counter() 
                                                 
                   
                    for row in range(i,i+3):
                        for col in range(j, j+3):
                                    
                            in_count[board[row][col]] += 1 if board[row][col] != "." else 0
                                            
                                                      
                            if in_count[board[row][col]] > 1:                      
                                
                                    return False
                print(num_count)
        
                    

                    

                        

        for i in range(len(board)):
            num_count=Counter()

            for j in range(len(board[0])):

                num_count[board[i][j]] += 1 if  board[i][j] != "." else 0

                if num_count[board[i][j]] > 1:
                     return False            
        
        return True
                        
        