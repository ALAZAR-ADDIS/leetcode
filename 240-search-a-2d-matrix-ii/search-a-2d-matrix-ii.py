class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for matr in matrix:
            l = - 1
            r = len(matr)
            if matr[0] >target:
                continue
            while l + 1 < r:

                mid = (l + r)//2

                if matr[mid] >= target:
                    r = mid
                else:
                    l = mid
            
            if r < len(matr) and matr[r] == target:
                return True
        return False
        