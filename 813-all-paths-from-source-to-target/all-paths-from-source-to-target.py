class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node,path):
            path.append(node)
            visited.add(node)

            for n in graph[node]:
                if n not in visited:
                    dfs(n,path)
            if path[-1] == len(graph) - 1:
                ans.append(path[::])
            path.pop()
            visited.remove(node)
        visited = set()
        ans = []
        dfs(0,[])
        return ans
                    

        