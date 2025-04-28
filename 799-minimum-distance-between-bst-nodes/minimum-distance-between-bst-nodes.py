# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 
            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)
            
        ans = []
        dfs(root)
        ans.sort()
        minn = float("inf")
        for i in range(len(ans) - 1):
            minn = min(minn,ans[i + 1] - ans[i])
        
        return minn


    
        