class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(node,color):

            visited[node] = color
            nColor = 0 if color else  1
            for n in grp[node]:
                if n not in visited:
                    val = dfs(n,nColor)
                    if not val:
                        return False
                elif visited[n] == color:
                    return False
            return True
            
        visited = defaultdict(str)
        grp = defaultdict(list)
        for x,y in dislikes:
            grp[x].append(y)
            grp[y].append(x)
        
        key = list(grp.keys())

        for k in key:
            if k not in visited:
                if not dfs(k,0):
                    return False
        return True