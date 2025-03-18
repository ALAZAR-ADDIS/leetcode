# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            new = TreeNode(val)
            return new
            
        if root.val < val:
            root.right = self.insertIntoBST(root.right,val)
        
        if root.val > val:
            root.left = self.insertIntoBST(root.left,val)

        return root

        # def helper(root,val):

        #     if not root:
        #         return TreeNode(val)


                      
        #     if root.val <  val :
        #         if not root.right:
        #             root.right = TreeNode(val)
        #             return root
        #         helper( root.right ,val)
                 
        #     else:
        #         if not root.left:
        #             root.left = TreeNode(val)
        #             return 
        #         helper( root.left ,val)

                 
        # if not root:
        #     return TreeNode(val)
        # helper(root,val)

        # return root

        