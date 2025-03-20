# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':



        def solve(root,minn,maxx):
            if not root:
                return None
            if root.val > minn.val and root.val >maxx.val:
                return solve(root.left, minn , maxx)
            elif  root.val < minn.val and root.val < maxx.val:
                return solve(root.right, minn , maxx)
            else:
                return root
            
            # if minn.val <= root.val <= maxx.val:
            #     if root.left and (minn.val < maxx.val < root.left.val ):
            #         return solve(root.left,minn,maxx)
            #     elif root.right and (root.right.val< minn.val < maxx.val ):
            #         return solve(root.right,minn,maxx)
            #     else:
            #         return root
            # else:

            #     if root.val > maxx.val:
            #         return solve(root.left,minn,maxx)
            #     else:
            #         return solve(root.right,minn,maxx)
        
        return solve(root,p,q)
                
                    
            

        # if not root:
        #     return None
        
        # if root == p or root == q:
        #     return root
        
        # left = self.lowestCommonAncestor(root.left,p,q)
        # right = self.lowestCommonAncestor(root.right,p,q)

        # if left and right :
        #     return root
        # return left if left else right
        