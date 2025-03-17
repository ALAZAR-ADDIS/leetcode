# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
       

        def solve(root):        
            
            if not root :
                return 0
            
            l = 1 + (solve(root.left))
            r = 1 + (solve(root.right))

            return max(l,r)
        
       
            
        return solve(root)

        