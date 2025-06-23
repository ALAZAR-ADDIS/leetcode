class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            heapq.heapify(grid[i])
        ans = 0
        
        for j in range(len(grid[0])):
            minn = grid[0][0]
            for i in range(len(grid)):
                minn = max(minn, grid[i][0])
                heapq.heappop(grid[i])
            
            ans += minn
        
        return ans
                        