class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        # def dfs(node):

        #     visited.add(node)
        #     no = 0
        #     ed = 0


        #     for n in graph[node]:
               
        #         if n not in visited:
        #             nod,e = dfs(n)
        #             no += nod
        #             ed += e
                
        #         if (node,n) not in edge  and (n,node) not in edge:
        #             edge.add((node,n))
        #             ed += 1
                    
        #     return [no + 1, ed]
                    
        
        # visited = set()
        # edge = set()
        # graph = defaultdict(list)
        # count = 0
       
        # for x,y in edges:
        #     graph[x].append(y)
        #     graph[y].append(x)
      
        
        
        # for i  in range(n):
        #     if i not in visited:
        #         no,ed = dfs(i) 
                      
        #         if ed == (no * (no - 1))/2:                    
        #             count += 1
        
        # return count



        def dfs(node,res):

            visited.add(node)
            res.append(node)           


            for n in graph[node]:
                if n not in visited:
                    dfs(n,res)
            
            
            return  res

        graph = defaultdict(list)
        visited = set()
        count = 0
        
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
       
        
        for i in range(n):
            if i not in visited:
               
                res = dfs(i,[])
                flag = True

                for n in res:
                    if len(res) - 1 != len(graph[n]):
                        flag = False
                
                if flag:
                    count += 1
        
        return count

           