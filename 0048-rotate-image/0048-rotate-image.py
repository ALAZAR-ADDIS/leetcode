class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            j=i+1
            while j<len(matrix):
                matrix[i][j],matrix[j][i]= matrix[j][i],matrix[i][j]
                j+=1

        
        for i in range(len(matrix)):
            rightpointer=len(matrix)-1
            leftpointer=0
            while leftpointer<rightpointer:
                matrix[i][leftpointer],matrix[i][rightpointer]= matrix[i][rightpointer],matrix[i][leftpointer]
                leftpointer+=1
                rightpointer-=1
        return matrix
           