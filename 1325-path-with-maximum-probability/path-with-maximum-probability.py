class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = defaultdict(list)

        for i in range(len(edges)):
            v,u = edges[i]

            graph[u].append((v,succProb[i]))
            graph[v].append((u,succProb[i]))
        
        ans = [-1] * n
        ans[start_node] = 1
        qu = deque()
        qu.append((start_node ,1))

        while qu: 
            for _ in range(len(qu)):
                node, w = qu.popleft()
                for n in graph[node]:
                    if n[0] != node:
                        if w * n[1] > ans[n[0]]:
                            qu.append((n[0], w * n[1]))
                            ans[n[0]] = w * n[1]
        print(ans)
        return ans[end_node ] if ans[end_node ] > 0 else 0
        
        