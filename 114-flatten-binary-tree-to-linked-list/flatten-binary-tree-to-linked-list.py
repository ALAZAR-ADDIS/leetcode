# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def solve(root):
            if not root:
                return None
            qu.append(root)
            
            solve(root.left)
            solve(root.right)

        qu = deque()
       
        prev = None
        dummy = TreeNode(0)
        curr = dummy
        solve(root)
        while qu:
            curr.right = qu.popleft()
            curr = curr.right
            curr.left = None
        return dummy.right
