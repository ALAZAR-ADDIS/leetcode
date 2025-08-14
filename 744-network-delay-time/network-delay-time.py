class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
       
        visited = set()
        graph = defaultdict(list)
        for x,h, t in times:
            graph[x].append((h,t))
        
        ans = 0
        heap =[(0,k)]
        while heap:
            w1,node = heapq.heappop(heap)
            if node  not in  visited:
                
                visited.add(node)
                ans = max(ans, w1)
                for no,w2 in graph[node]:
                    if no not in visited:
                            heapq.heappush(heap,(w1 + w2, no))
        if len(visited) == n:
            return ans
        return -1
        
        

        