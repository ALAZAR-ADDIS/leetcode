class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        # xy = 0
        # xz =0
        # yz = 0

        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j]:
        #             xy += 1
        #     xz += max(grid[i])
       
        
        # for j in range(len(grid[0])):
        #     temp = - float("inf")
        #     for i in range(len(grid)):                                 
        #         temp = max(temp, grid[i][j])
       
        #     yz += temp
       

        # return xy + xz + yz

        xy = 0
        xz =0
        yz = 0

        for i in range(len(grid)):
                xz += max(grid[i])
       
        
        for j in range(len(grid[0])):
            temp = - float("inf")
            for i in range(len(grid)):
                if grid[i][j]:
                    xy += 1                                 
                temp = max(temp, grid[i][j])
       
            yz += temp
       

        return xy + xz + yz  
    
        