# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:




        def helper(root,start,end):
            if not root:
                return True
            if not(start < root.val < end):
                return False
            
            left = helper(root.left,start,root.val)
            right = helper(root.right,root.val,end)
            
            return  left and right
        return helper(root,-float("inf"),float("inf"))

        # def solve(root):
        #     if not root:
        #         return
            
        #     solve(root.left)
        #     stack.append(root.val)
        #     solve(root.right)

        # stack = []
        # solve(root)
        # temp = stack[0]
        # for i  in range(1,len(stack)):
        #     if stack[i] <= temp:
        #         return False
        #     temp = stack[i]
        # return True
        
        