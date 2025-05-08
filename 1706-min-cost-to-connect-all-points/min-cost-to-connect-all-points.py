class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mapp = defaultdict(list)

        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i + 1,len(points)):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1 - y2)
                mapp[i].append([dist,j])
                mapp[j].append([dist,i])
        
        minH=[[0,0]]
        visited = set()
        cost = 0
        while len(visited) < len(points):
            dist,i = heapq.heappop(minH)

            if i in visited:continue
            cost += dist
            visited.add(i)

            for d,j in mapp[i]:
                if j not in visited:
                    heapq.heappush(minH,[d,j])
        return cost
                    

        