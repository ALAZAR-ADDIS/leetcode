# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def solve(root):
            nonlocal summ

            

            if not root:
                return 
            
            
            solve(root.right)            
            
            root.val = summ + root.val
            summ = root.val
            

            solve(root.left)

        summ = 0
        
        solve(root)
        print(summ)
        return root