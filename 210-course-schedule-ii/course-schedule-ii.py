class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # def dfs(node):
        #     if color[node] == 1:               
        #         return False
            
        #     color[node] = 1

            

        #     for n in graph[node]:
        #         if color[node] == 2:
        #             continue
                
        #         if  not dfs(n):
        #             return False
           
        #     color[node] = 2                
        #     order.append(node)
        #     return True

        # graph = defaultdict(list)
        # order = []
        # color = defaultdict(int)

        # for cor,pre in prerequisites:
        #     graph[cor].append(pre)

        # for i in range(numCourses):
            

        #     if color[i]:
        #         continue
       

        #     if  not dfs(i) :
        #         return []
        # return order


        qu = deque()
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for cor,pre in prerequisites:
            graph[pre].append(cor)
            indegree[cor] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                qu.append(i)

        order = []
        
        while qu:

            node = qu.pop()
            order.append(node)
            
            

            for n in graph[node]:                
                indegree[n] -= 1

                if indegree[n] == 0:
                    qu.append(n)

        if len(order) != numCourses:
            return  []
        return order
            



        
        
        
        








     
        
            