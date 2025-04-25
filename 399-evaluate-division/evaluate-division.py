class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def dfs(node,need):
            visited.add(node)

            for n in graph[node]:
                
                if n  == need:  
                                    
                    return val[(node,n)]
                else:
                    if n not in visited:
                        res = dfs(n,need)
                        
                        if res != -1:
                            return val[(node,n)] * res
            return -1

        val = defaultdict(int)
        graph = defaultdict(list)
        ans = []
        for index,pair in enumerate(equations):
            
            a, b  = pair
            val[(a,b)] = values[index]
            val[(b,a)] = 1/values[index]
            graph[a].append(b)
            graph[b].append(a)

        for node,need in queries:
            visited = set()            
            

            ans.append(dfs(node,need))
        return ans

            
            
           
            
            
            
        
       

        
        