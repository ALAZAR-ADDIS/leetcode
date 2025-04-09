class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            visited.add(node)

            for n in nodes[node]:
                if n not in visited:
                    dfs(n)



        nodes = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if  isConnected[i][j]:
                    nodes[i].append(j)
                    
        visited = set()
        count  = 0

        for node in nodes:
            if node not in visited:
                dfs(node)
                count += 1
        return count
            
            