class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        count = defaultdict(int)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    row = f"row{j}One"
                    count[row] += 1
                else:
                    row = f"row{j}Zero"
                    count[row] += 1
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if grid[j][i]:
                    col = f"col{j}One"
                    count[col] += 1
                else:
                    col = f"col{j}Zero"
                    count[col] += 1
            

                
                # if grid[i][j]:
                #     col = f"col{j}One"
                #     row = f"row{i}One"
                #     count[col] += 1
                #     count[row] += 1
                # else:
                #     col = f"col{j}Zero"
                #     row = f"row{i}Zero"
                #     count[col] += 1
                #     count[row] += 1
       

        ans = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # print(i,j)
                # print(count[f"col{i}One"] , count[f"row{j}One"] , count[f"col{i}Zero"] , count[f"row{j}Zero"])
                ans[i][j] = (count[f"col{i}One"] + count[f"row{j}One"]) - (count[f"col{i}Zero"] + count[f"row{j}Zero"])
        return ans

                    
        