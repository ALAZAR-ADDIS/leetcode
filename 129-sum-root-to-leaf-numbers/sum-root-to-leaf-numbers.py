# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:



        def solve(root,val):
            nonlocal ans

            if not root:
                return 0
            val = 10 * val +  int(root.val)
            if not root.right and not root.left:
                ans += val
            solve(root.left,val)
            solve(root.right,val)

        ans = 0 
        solve(root,0)        
        return ans

             

        