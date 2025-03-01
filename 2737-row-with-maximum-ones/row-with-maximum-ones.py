class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ones = sum(mat[0])
        index = 0
        for i,row in enumerate(mat):

            if ones < sum(row):
                index = i
                ones = sum(row)
            
        return [index,ones]

        