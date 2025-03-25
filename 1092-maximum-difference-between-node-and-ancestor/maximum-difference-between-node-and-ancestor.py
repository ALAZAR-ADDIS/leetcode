# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def solve(root,maxx,minn):

            nonlocal ans
            if not root:
                return 
            
            ans = max(ans,abs(maxx - root.val),abs(minn- root.val))

            maxx = max(maxx,root.val)
            minn = min(minn,root.val)
            solve(root.left,maxx,minn)      
        
            solve(root.right,maxx,minn)
           

        ans = -float("inf")


        solve(root,root.val,root.val)

        return ans

        
   


           

        