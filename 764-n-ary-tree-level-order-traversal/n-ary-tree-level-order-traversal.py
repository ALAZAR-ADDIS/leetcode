"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        qu = deque()
        qu.append(root)
        ans = []
        while qu:
            temp = []
            for _ in range(len(qu)):

                node = qu.popleft()
                temp.append(node.val)
                for n in node.children:
                    if n :
                        qu.append(n)
            
            ans.append(temp)
        return ans
        