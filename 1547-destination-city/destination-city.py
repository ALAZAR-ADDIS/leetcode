class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        path = defaultdict(int)

        for x,y in paths:
            path[x] += 1
        
        for x,y in paths:
            if not path[y]:
                return  y
        