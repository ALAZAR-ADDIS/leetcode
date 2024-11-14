class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        col=len(img[0])
        row=len(img)
        k=0
        newMatr=[[0]*col for _ in range(row)]
        length=col*row
        while k<length:
            col_n=k%col
            row_n=k//col
            total,count=0,0
            for i in range(row_n-1,row_n+2):
                for j in range(col_n-1,col_n+2):
                    if i<0 or j<0 or j>=col or i>=row:
                        continue
                    total+=img[i][j]
                    count+=1
            
            newMatr[row_n][col_n]=total//count
            k+=1
        return newMatr
    


        