# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def solve(path,node):
            if not node:              
                return 

            
            path.append(node.val)
            
            if path and   sum(path) == targetSum  and not (node.left or node.right) :
                    ans.append(path[::])
            
            solve(path,node.left)
            solve(path, node.right)
            path.pop()
        
        ans = []
        solve([],root)
        return ans 
        