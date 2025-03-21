# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def helper(root,summ ,leaf):
            if not root:
                return  leaf and summ == targetSum
            summ += root.val 

            left = helper(root.left,summ,False if root.right or root.left else True)
            right = helper(root.right,summ,False if root.right or root.left else True)

            return left if left else right
        if not root:
            return False
        return helper(root,0,False if root.right or root.left else True)
        