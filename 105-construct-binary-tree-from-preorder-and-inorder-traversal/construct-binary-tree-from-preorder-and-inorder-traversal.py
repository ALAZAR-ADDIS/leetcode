# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def solve(left,right,pre):
            if left >= right:
                return None
          
            root_index = map_inorder[preorder[pre]]
            node = TreeNode(inorder[root_index])

            node.left = solve(left,root_index,pre + 1)
            node.right = solve(root_index + 1, right, pre +  root_index - left + 1)

            return node


        map_inorder = {n:i for i,n in enumerate(inorder)}

        

        
        
        return solve(0,len(preorder),0)



            

    

      
        