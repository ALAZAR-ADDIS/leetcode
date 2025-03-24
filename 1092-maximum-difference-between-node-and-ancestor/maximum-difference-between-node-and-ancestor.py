# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def solve(root):

            nonlocal ans
            nonlocal maxx
            nonlocal minn
            if not root:
                return 
            
            ans = max(ans,abs(maxx - root.val),abs(minn- root.val))

            tMax = max(maxx,root.val)
            tMin = min(minn,root.val)

            maxx = tMax
            minn = tMin

            print(tMax,tMin)
            print(root.val)


            solve(root.left)

            maxx = tMax
            minn = tMin
        
            solve(root.right)
           

        ans = -float("inf")

        maxx = root.val
        minn = root.val

        solve(root)

        return ans

        
   


           

        