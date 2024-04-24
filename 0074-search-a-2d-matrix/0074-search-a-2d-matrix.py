class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        right=len(matrix)*len(matrix[0])-1
        while(right>=left):
            mid=(right+left)//2
            firdim=mid//(len(matrix[0]))
            secdim=(mid)%len(matrix[0])
            if(matrix[firdim][secdim]==target):
                return True
            elif (matrix[firdim][secdim]<target):
                left=mid+1
            else:
                right=mid-1
        return False