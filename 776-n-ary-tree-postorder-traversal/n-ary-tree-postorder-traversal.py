"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def solve(root):
            if not root:
                return 
            
            for n in root.children:
                solve(n)
            ans.append(root.val)
        
        ans = []
        solve(root)
        return ans
        