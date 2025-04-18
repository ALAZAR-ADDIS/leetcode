class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        def dfs(node):
            
            visited.add(node)
            for i in rooms[node]:
                 keys.add(i )
           

            for n in rooms[node]:
                if n not in  visited :
                    if n in keys:
                        visited.add(n)
                        dfs(n)

        keys = set()
        visited = set()
        
        dfs(0)
        
        for i in range(1,len(rooms)):
            if i not in visited:
                return False
        return True
        



        