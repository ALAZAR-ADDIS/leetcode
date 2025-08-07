# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def solve(path,node,root):
            if not node:
                if path and sum(path) == targetSum  and not( root.left or root.right) :

                    ans.append(path[::])
                return 
            
            path.append(node.val)
            solve(path,node.left,node)
            if node.right:
                 solve(path, node.right,node)
            path.pop()
        
        ans = []
        solve([],root,None)
        return ans 
        