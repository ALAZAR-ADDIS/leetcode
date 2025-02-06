class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # ans=[[]  for i in range(len(matrix[0]))]

        # for _list in matrix:

        #     for i in range(len(_list)):
        #         ans[i].append(_list[i])
        # return ans

        #approch 2

        ans = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for i  in  range(len(matrix)):
            for j in range(len(matrix[0])):
                ans[j][i] = matrix[i][j]

        return ans

                
        