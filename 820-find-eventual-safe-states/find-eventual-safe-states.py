class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        def dfs(node):
            if color[node]:
                return False
            color[node] = 1

            for n in graph[node]:
                if color[n] == 2:
                    continue

                if not dfs(n):
                    return False
            
            color[node] = 2
            order.append(node)
            return True

        color = defaultdict(int)
        order = []
        
        for i in range(len(graph)):
            if  color[i] == 0:
                dfs(i)
           

        order.sort()
        return order