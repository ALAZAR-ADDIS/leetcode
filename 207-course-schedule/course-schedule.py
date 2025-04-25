class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # def cycleDetector(child):
        #     visited[child] = "gray"

            
        #     for n in graph[child]:
        #         if n not in visited:
        #             val   = cycleDetector(n)
        #             if not val:
        #                 return False
        #         elif visited[n] == "gray":                   
        #             return False
                
        #     visited[child] = "black"
        #     return True



            # visited.add(child)

            # for n in graph[child]:
            #     if n not in visited:
            #         val = cycleDetector(n,child)
            #         if val :
            #             return True
            #     else:
            #         return True
            # return False

        # graph = defaultdict(list)
        # visited = defaultdict(str)

        # for cor,pre in prerequisites:
        #         graph[pre].append(cor)

        # key = list(graph.keys())
        # for g in range(numCourses):
        #         if not cycleDetector(g):
        #             return False

        # return True



        indegree = defaultdict(int)
        graph = defaultdict(list)
        qu =  deque()

        for x,y in  prerequisites:
            graph[y].append(x)
            indegree[x] += 1
        
        for i in range(numCourses):            
            if indegree[i] == 0:
                qu.append(i)

        count = 0       


        while qu :

            node = qu.popleft()
            count += 1

            for n in graph[node]:
                indegree[n] -= 1
                
                if indegree[n] == 0:
                    
                    qu.append(n)
        print(count)
        
        if count == numCourses:
            return True
        return False
            



        