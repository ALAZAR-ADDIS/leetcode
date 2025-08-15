class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
 
       
        for i in range(1,100000 + 1):
          
            if len(graph[i]) >= 2:
               return i
     

        