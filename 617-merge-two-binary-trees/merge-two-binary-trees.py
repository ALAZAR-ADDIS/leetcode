# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:


        def helper(root1,root2):

            if not root1 or not root2:
                return 

                       

            helper(root1.left,root2.left)
            helper(root1.right,root2.right)
            
            root1.val = root1.val + root2.val

            if not root1.left and  root2.left:
                root1.left = root2.left
            if not root1.right and  root2.right:
                root1.right = root2.right
        if not root1: return root2 
        helper(root1,root2)
        return root1
            
            
           
            
            

           