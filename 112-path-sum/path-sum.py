# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def helper(root,summ ):
            if not root:
                return  False
            summ += root.val 

            if summ == targetSum and not root.left and not root.right:
                return True

            left = helper(root.left,summ)
            right = helper(root.right,summ)

            return left if left else right
      
        return helper(root,0)
        