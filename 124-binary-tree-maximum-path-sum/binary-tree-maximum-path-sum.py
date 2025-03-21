# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:


        def solve(root):
            nonlocal maxx
            if not root:
                return 0
            
            left = solve(root.left)
            right = solve(root.right)

            left = max(0,left)
            right = max(0,right)

            maxx = max(maxx,left + right + root.val)

            return root.val + max(left,right)


            # if left< 0 and right < 0:
            #     maxx = max(root.val,maxx)
            #     return root.val
            # elif left < 0:
            #     maxx = max(root.val + right,maxx)
            #     return root.val + right
            # elif right < 0:
            #     maxx = max(root.val + left,maxx)
            #     return root.val + left
            # else:
            #      maxx = max(root.val + left + right,maxx)
            #      return root.val + max(left,right)


          
           


        maxx = -float("inf")
        solve(root)
        return maxx




        