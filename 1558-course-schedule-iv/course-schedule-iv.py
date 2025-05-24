class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for x,y in prerequisites:
            indegree[y] += 1
            graph[x].append(y)

        qu = deque()
        mapp = defaultdict(set)

        for i in range(numCourses):
            if indegree[i] == 0:
                qu.append(i)

      
        while qu:
            leng = len(qu)         
            node = qu.popleft()
            for n in graph[node]:
                mapp[n].add(node)
                for pre in mapp[node]:
                    mapp[n].add(pre)
                indegree[n] -= 1
                if indegree[n] == 0:
                    qu.append(n)
       
        
        
        ans = []
        for x,y in queries :
            f = False
            for i in mapp[y]:
                if x == i:
                    f = True
                    ans.append(True)
                    break
            if not f:
                ans.append(False)
            
        return ans


        #dfs solution

        # def dfs(node, org):
        #     if node == org:
        #         return True

        #     visited.add(node)

        #     for n in graph[node]:
        #         if n not in visited:
        #             val = dfs(n, org)
        #             if val:
        #                 return True
        #     return False
        # ans = []        
        # for x,y in queries :
        
        #     visited  = set()
        #     ans.append(dfs(x,y))

        return ans

                



        