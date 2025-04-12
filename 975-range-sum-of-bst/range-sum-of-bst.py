# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:


        def solve(root):
            if not root:
                return 0
            
            left = solve(root.left)
            right = solve(root.right)
            curr = root.val if low <= root.val <= high else 0

            return left  + right + curr
        return solve(root)

        