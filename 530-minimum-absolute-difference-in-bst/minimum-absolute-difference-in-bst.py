# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right) 
        arr = []
        dfs(root)
        minn = float("inf")
        for i in range(len(arr) - 1):
            minn = min(minn, arr[i + 1] - arr[i])
        return minn
            
            


        