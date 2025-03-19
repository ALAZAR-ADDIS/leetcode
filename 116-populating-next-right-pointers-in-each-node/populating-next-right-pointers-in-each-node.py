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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        def helper(qu):
            if not qu:
                return
            
            leng = len(qu)
            prev = None
            
            while leng > 0:
                poped = qu.pop()
                poped.next = prev
                prev = poped

                if poped.right:
                    qu.appendleft(poped.right)
                if poped.left:
                    qu.appendleft(poped.left)
                leng -= 1
            helper(qu)
        if not root:
            return 
        
        q = deque()
        q.append(root)
        helper(q)

        return root


        