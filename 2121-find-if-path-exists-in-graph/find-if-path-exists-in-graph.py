class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        def solve(node, visited):
            if node == destination:
                return True
            
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    res  = solve(i,visited)  
                    if res:
                        return  True 
            return False
        return solve(source,set())
        