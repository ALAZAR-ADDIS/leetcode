class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(len(original)):
            graph[original[i]].append((changed[i],cost[i]))
        print(graph)
        def shortest(sorce,des):
            heap = [(0,sorce)]          
            dis = {chr(97 + i):float("inf") for i in range(26)}
            dis[sorce] = 0
        

            while heap:
                
                w1, node = heappop(heap)

                for n,w2 in graph[node]:
                
                   if n in  dis and dis[n] > w1  + w2:
                        dis[n] = w1  + w2
                        heappush(heap,(dis[n],n))
            return dis[des] 

        ans = 0
        computed = {}
        for i in range(len(source)):
            curr = source[i] + target[i]
            if source[i] != target[i]:
                if curr in computed:
                    ans += computed[curr]
                    continue

                val =  shortest(source[i],target[i])
                if val == float("inf"):
                    return -1
                computed[curr] = val
                ans += val
        return ans