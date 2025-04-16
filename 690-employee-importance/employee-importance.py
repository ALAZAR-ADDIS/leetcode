"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        def dfs(node,founded = False):
            if node.id == id:
                founded = True
            
            visited.add(node.id)

           
            count = 0
            print(node.subordinates)
            for n in node.subordinates:
                if n not in visited:
                    count += dfs(graph[n][0],founded)
            print(count)
            if founded:
                return count + node.importance
            return count
        
        graph = defaultdict(list)
        visited = set()

        for n in employees:
            graph[n.id].append(n)


        
        return dfs(graph[id][0])
         
        
           
        