class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = -1 
        r = len(matrix) * len(matrix[0]) 
        row = 0
        col = 0

        while l + 1 < r:
            mid = (l + r)//2

            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            print(row,col)

            if matrix[row][col] >= target:
                r = mid
            else:
                l = mid
        
        row = r // len(matrix[0])
        col = r % len(matrix[0])

        return True if r < len(matrix) * len(matrix[0])  and  matrix[row][col] == target else False