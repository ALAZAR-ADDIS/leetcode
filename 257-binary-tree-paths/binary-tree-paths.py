# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def dfs(root,path,par):
            if not root:
                if not par or (not par.left and not par.right):
                    if tuple(path) not in added:
                        added.add(tuple(path))
                        ans.append("->".join(map(str,path)))
                return 
            
            path.append(root.val)
            dfs(root.left,path,root)            
            dfs(root.right,path,root)

            path.pop()
        
        ans = []
        added = set()
        dfs(root,[],None)
        return ans
            
        