"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        def solve(root):
           
            
            maxx = 0
            
            for c in root.children:
                
               maxx = max(maxx,solve(c))  
        
            return maxx + 1

        return solve(root) if root else 0

        