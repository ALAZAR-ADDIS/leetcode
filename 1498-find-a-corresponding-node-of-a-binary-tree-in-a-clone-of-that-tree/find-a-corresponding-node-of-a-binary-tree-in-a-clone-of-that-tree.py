# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def find(node):
            if not node:
                return 
            
            if node.val == target.val:
                return node
            
            val = find(node.left)
            if val:
                return val
            val = find(node.right)
            if val :
                return val
        
        return find(cloned)
        