class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        
        self.mat = [[0]*(col + 1) for _ in range(row + 1)]

        for i in range(row):
            for j in range(col):
                self.mat[i + 1][j + 1] = matrix[i][j] + self.mat[i][j + 1] + self.mat[i + 1][j ] - self.mat[i][j]
     
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return self.mat[row2 + 1][col2 + 1] + self.mat[row1  ][col1  ] - self.mat[row1][col2 + 1] - self.mat[row2 + 1][col1]

      

        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)