# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def solve(root):
            
            if not root:
                return -1
            
            left =  solve(root.left)
            right =  solve(root.right)

            maxx[0] = max(left + right + 2,maxx[0])

            return max(left,right) + 1
        # print(solve(root.left))
        # print(solve(root.right))
        # return  solve(root.left) + solve(root.right)

        maxx = [-float("inf"),]
        solve(root)
        return maxx[0]


        
        