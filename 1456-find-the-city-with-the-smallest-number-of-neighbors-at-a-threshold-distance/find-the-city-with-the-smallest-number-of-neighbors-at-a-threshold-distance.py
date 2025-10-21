class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for i,j,w in edges:
            graph[i].append((j,w))
            graph[j].append((i,w))
        

        def solve(start,n):
            dis = [float("inf") for _ in range(n)]
            dis[start] = 0
            heap = [(0,start)]
           

            while heap:

                w1, node = heappop(heap)
                for n,w2 in graph[node]:
                    if w1 + w2 < dis[n]:
                        dis[n] = w1 + w2
                        heappush(heap, (dis[n], n))
            return dis
                        


        prev = float("inf")
        ans = 0
        for i in range(n):
            count = 0
            sol = solve(i,n)
        
            for j in sol:
                
                if j <= distanceThreshold:
                    count += 1
        
            if count <= prev:
                prev = count
                ans = i
        return ans
        