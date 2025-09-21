"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        qu = deque()
        qu.append(root)
        if not root:
            return root
        while qu:
            leng  = len(qu)
            for _ in range(len(qu)):
                node = qu.popleft()

                if node.left:
                    qu.append(node.left)
                
                if node.right:
                    qu.append(node.right)
                
                if _ != leng - 1:
                    node.next = qu[0]
                else:
                    node.next = None
        
        return root
        