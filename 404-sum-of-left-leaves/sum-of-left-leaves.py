# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:


        def solve(root):
            nonlocal total
            if not root:
                return 
            
            if root.left and not root.left.right and not root.left.left:
                total += root.left.val
            
            solve(root.left)
            solve(root.right)
        total = 0
        solve(root)

        return total
        