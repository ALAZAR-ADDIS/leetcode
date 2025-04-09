class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def cycleDetector(child):
            visited[child] = "gray"

            
            for n in graph[child]:

                if n not in visited:
                    val   = cycleDetector(n)
                    if not val:
                        return False
                elif visited[n] == "gray":
                   
                    return False
                
            visited[child] = "black"
            return True



            # visited.add(child)

            # for n in graph[child]:
            #     if n not in visited:
            #         val = cycleDetector(n,child)
            #         if val :
            #             return True
            #     else:
            #         return True
            # return False

        graph = defaultdict(list)
        visited = defaultdict(str)

        for cor,pre in prerequisites:
                graph[pre].append(cor)

        key = list(graph.keys())
        for g in key:
                if not cycleDetector(g):
                    return False

        return True



        