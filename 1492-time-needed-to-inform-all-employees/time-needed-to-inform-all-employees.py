class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        def dfs(node):

            time = 0
            for n in graph[node]:
                time = max(time , informTime[node] + dfs(n))
            return time
                

        graph = defaultdict(list)
        for i in range(len(manager)):
            graph[manager[i]].append(i)
        
        
        return dfs(headID)
        