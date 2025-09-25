# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = defaultdict(int)
        def dp(root,take):
            if not root:
                return 0
            
                     
         
            
            state = (root,take)
            if state in memo:
                return memo[state]
            left = dp(root.left, not take)
            right = dp(root.right, not take)
            
            if take :
                memo[state] = max(dp(root.left,False), left)  + max(dp(root.right,False), right)+ root.val
            else:
                memo[state] = max(dp(root.left,False), left)  + max(dp(root.right,False), right)
            
                
            return memo[state]
        
        
        return max(dp(root, True),dp(root,False))

            
                
                
        