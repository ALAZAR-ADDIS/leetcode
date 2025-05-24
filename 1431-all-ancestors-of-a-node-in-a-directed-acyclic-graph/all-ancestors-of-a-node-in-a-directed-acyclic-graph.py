class Solution:
    def getAncestors(self, size: int, edges: List[List[int]]) -> List[List[int]]:
        indegree = defaultdict(int)
        graph = defaultdict(list)

        for x,y in edges:
            indegree[y] += 1
            graph[x].append(y)
        
        qu  = deque()        
        for i  in range(size):
            if indegree[i] == 0:
                qu.append(i)
        
            
        mapp = defaultdict(set)

        
       
        
        while qu:
            node = qu.popleft()
            for n in graph[node]:
                mapp[n].add(node)
                for pre in mapp[node]:
                    mapp[n].add(pre)
                indegree[n] -= 1
                if indegree[n] == 0:
                    qu.append(n)
        
        ans = []
        for i in  range(size):
            ans.append(sorted(list(mapp[i])))
        return ans


        
        