# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def solve(root):
            if not root:
                return None
            
            
            left = solve(root.left)

            count[0] += 1
            if count[0] == k -1:
                return root

            right =  solve(root.right)

            return left if left else right
        count = [-1,]
        return solve(root).val


        # def solve(root):
        #     if not root:
        #         return 
            
        #     solve(root.left)
        #     ans.append(root.val)
        #     solve(root.right)


        # ans = []
        # solve(root)
        # return ans[k-1]

        