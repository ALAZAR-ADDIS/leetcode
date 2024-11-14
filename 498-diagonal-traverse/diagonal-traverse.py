class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        col=len(mat[0])
        row=len(mat)
        ans=[]
        Up=True
        cur_col=cur_row=0
        while len(ans)<col*row:
            if Up:
                while cur_row>=0 and cur_col<col :
                    ans.append(mat[cur_row][cur_col])
                    cur_row-=1
                    cur_col+=1
                if cur_col==col:
                   cur_row+=2
                   cur_col-=1
                else:
                    cur_row+=1
                Up=False
                
            else:
                while cur_col>=0 and cur_row<row :
                    ans.append(mat[cur_row][cur_col])
                    cur_col-=1
                    cur_row+=1
                if cur_row==row:
                   cur_col+=2
                   cur_row-=1
                else:
                    cur_col+=1
                Up=True
            
        return ans 