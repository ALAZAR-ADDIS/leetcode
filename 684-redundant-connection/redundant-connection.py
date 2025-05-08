class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]: 
        def find(x):
            if parent[x] == x:
                return x
            
            root = find(parent[x])
            parent[x] = root
            return root
        def union(x,y):
            par = find(x)
            par2 = find(y)

            if par == par2:
                return False

            if par != par2:
                if rank[par] == rank[par2]:
                    parent[par] = par2
                    rank[par2] += 1
                elif rank[par] > rank[par2]:
                    parent[par2] = par
                else:
                    parent[par] = par2

            return True
        parent = [i for i in range(len(edges) + 1)]
        rank = {i:0 for i in range(len(edges) + 1)}
        
        for x,y in edges:
            if not union(x,y):
                return [x,y]

        