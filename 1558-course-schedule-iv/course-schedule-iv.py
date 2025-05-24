class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        # indegree = defaultdict(int)

        for x,y in prerequisites:
            # indegree[y] += 1
            graph[x].append(y)

        # qu = deque()
        # mapp = defaultdict(int)

        # for i in range(numCourses):
        #     if indegree[i] == 0:
        #         qu.append(i)

        # l = 1
        # while qu:
        #     leng = len(qu)
        #     for  _ in range(leng):
        #         node = qu.popleft()
        #         for n in graph[node]:
        #             indegree[n] -= 1
        #             if indegree[n] == 0:
        #                 mapp[n]= l
        #                 qu.append(n)
        #     l += 1
        # print(mapp)
        
        # ans = []
        # for x,y in queries :
        #     if mapp[x] < mapp[y]:
        #         ans.append(True)
        #     else:
        #         ans.append(False)
        # return ans

        def dfs(node, org):
            if node == org:
                return True

            visited.add(node)

            for n in graph[node]:
                if n not in visited:
                    val = dfs(n, org)
                    if val:
                        return True
            return False
        ans = []        
        for x,y in queries :
        
            visited  = set()
            ans.append(dfs(x,y))

        return ans

                



        