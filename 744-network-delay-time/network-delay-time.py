class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        heap = [(0,k)]
        dis = {n:float("inf") for n in range(1,n + 1)}
        dis[k] = 0

        graph = defaultdict(list)
        for u,v, t in times:
            graph[u].append((v,t))

        while heap:
            w1, node = heappop(heap)
            for u,w2 in graph[node]:
                if dis[u] > w1 + w2:
                    dis[u] = w1 + w2
                    heappush(heap,(dis[u],u))
       
        for i in range(1,n + 1):
            if dis[i] == float('inf'):
                return -1
        return max(dis.values())

            
        

        
        

        