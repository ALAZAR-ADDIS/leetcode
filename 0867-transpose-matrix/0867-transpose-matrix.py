class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        matrix2=[]
        matrix3=[]
        for i in range(len(matrix[0])):
            matrix2=[]
            for j in range(len(matrix)):
                matrix2.append(matrix[j][i])
            matrix3.append(matrix2) 
            
            
        return matrix3