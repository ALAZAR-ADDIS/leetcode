class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def sorter(cord):
            x,y=cord
            return x**2 + y**2
        points.sort(key=sorter)
        return points[0:k]
    
