# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def solve(root,maxx,minn):

            if not root:
                return  -float("inf")
            
            

            maxx = max(maxx,root.val)
            minn = min(minn,root.val)

            left = solve(root.left,maxx,minn)  
        
            right =solve(root.right,maxx,minn)

            return max(maxx- minn,left,right)   

        


       

        return  solve(root,root.val,root.val)

        
   


           

        