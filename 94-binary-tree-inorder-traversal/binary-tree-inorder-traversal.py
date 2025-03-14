# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:



        result = []

        def solve(root):

            if root:
                solve(root.left)
                result.append(root.val)
                solve(root.right)
            return result
        return solve(root)

        