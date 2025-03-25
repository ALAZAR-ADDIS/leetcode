# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        def solve(root):
            nonlocal ans
            if not root:
                return[0,0]
            
            left = solve(root.left)
            right = solve(root.right)

            count = left[1] + right[1] + 1
            vals = left[0] + right[0] + root.val

            print(ans)
            ans += 1 if  vals//count == root.val else 0
            print(vals/count ,root.val)
            print(ans)

            return [vals ,count ]

        ans = 0
        solve(root)
        return ans
        

        