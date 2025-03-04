class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 1
        
        points.sort(key = lambda x : x[1])
        start= points[-1][0]
        end = points[-1][1]
        
    
        for i in range(len(points)-2,-1,-1):
           
            if start <=  points[i][1] <= end:
               
                start = max(start, points[i][0])
                
            else:
                ans += 1                      

                start= points[i][0]
                end = points[i][1]
            
           
        return ans

        