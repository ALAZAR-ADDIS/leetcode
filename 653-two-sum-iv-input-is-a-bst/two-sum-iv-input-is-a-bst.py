# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def solve(root):
            

            if not root:
                return False
       

            if k - root.val  in ans:
                return True
          
            ans.add(root.val)
            
            left = solve(root.left)
            if left :
                return True

            right = solve(root.right)
            if right :
                return True
            
            return False
            
    

        ans = set()
        # ans.add(0)
        val = solve(root)
        
        return val
        