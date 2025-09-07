# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        nodes = 1
        qu = deque()
        qu.append(root)
        level = 1
        if not root:
            return 0

        while qu:           
            
            
            for _ in range(len(qu)):
              
                node = qu.popleft()

                if node.left:
                    qu.append(node.left)
                if node.right :
                    qu.append(node.right)
                if not node.left and not node.right :
                    
                    return level
            level += 1
      