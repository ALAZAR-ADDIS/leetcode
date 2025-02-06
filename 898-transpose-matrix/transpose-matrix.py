class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[[]  for i in range(len(matrix[0]))]

        for _list in matrix:

            for i in range(len(_list)):
                ans[i].append(_list[i])
        return ans

                
        