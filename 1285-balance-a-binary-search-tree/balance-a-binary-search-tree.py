# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:



        def Trav(root):
            if not root:
                return             
            values.append(root.val)
            Trav(root.left)
            Trav(root.right)

        
        def insert(val,root):

            if not root:
                return TreeNode(val)

            if root.val > val:
                 root.left = insert(val,root.left)

            else:
                root.right = insert(val,root.right)
            
            return root
        
        def makeBalance(l,r):
            nonlocal root
            if l <  r: 
                mid = ( l + r)//2

                root = insert(values[mid],root)
                makeBalance(l, mid)
                makeBalance(mid + 1, r)

        
        values = []
        Trav(root)
        values.sort()

        root = None
        print(root)
        makeBalance(0,len(values))
        return root
        
        