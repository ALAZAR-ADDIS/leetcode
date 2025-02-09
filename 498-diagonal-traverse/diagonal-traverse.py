class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        is_up = True
        ans = []
        i = 0
        j = 0

        while i < len(mat) and j <len(mat[0]):

            if is_up:
                while i >= 0 and j < len(mat[0]):
                    ans.append(mat[i][j])
                    i -= 1
                    j += 1
                
                if j >= len(mat[0]):
                    i += 2
                    j -= 1
                else:
                    i += 1
                is_up = False
                
            else:

                while j >= 0 and i< len(mat):
                    ans.append(mat[i][j])
                    j -= 1
                    i += 1
                
                if i >= len(mat):
                    i -= 1
                    j += 2
                else:
                    j += 1        

                is_up = True
                

        return ans
