# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def helper(qu):
            if not qu:
                return
            
            leng = len(qu)
            temp = []

            while leng > 0:
                poped = qu.popleft()
                temp.append(poped.val)

                

                if poped.left:
                    qu.append(poped.left)
                if poped.right:
                    qu.append(poped.right)
                leng -= 1
            ans.append(temp)
            helper(qu)

        if not root:
            return []
        
        qu = deque()
        qu.append(root)
        ans = []

        helper(qu)
    

        return ans[::-1]
        

                
        