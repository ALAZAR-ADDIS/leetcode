# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:


        qu = deque()
        qu.append(root)
        val = root.val

        while qu:

            node = qu.popleft()
            if node.val != val:
                    return False
            

            if node.left:              
                qu.append(node.left)

            if node.right:             

                qu.append(node.right)
        return True
            

            
        