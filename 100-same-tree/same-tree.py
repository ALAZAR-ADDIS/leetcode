# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if (p and not  q) or (q and not p):
            return False
       
        
        if q.val != p.val:
            return False
        
        val1 = self.isSameTree(p.left,q.left)
        val2 = self.isSameTree(p.right,q.right)

        return val1 and val2

        