class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        indegree = defaultdict(int)
        

        for x,y in edges:
            indegree[y] += 1
        
        qu = deque()
        
        for i in range(n):            
            if indegree[i] == 0:
                qu.append(i)
       
        if len(qu) != 1:
            return -1
        return list(qu)[0]
        