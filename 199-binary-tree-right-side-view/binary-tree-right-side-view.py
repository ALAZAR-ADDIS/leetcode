# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def solve(qu):
            if not qu:
                return 
            
            temp = 0
            leng = len(qu)

            while leng > 0:
                poped = qu.popleft()
                temp = poped.val

                if poped.left:
                    qu.append(poped.left)

                if  poped.right:
                    qu.append(poped.right)
                leng -= 1
           
            ans.append(temp)

            solve(qu)





        if not root:
            return []
        ans = []
        
        q = deque()
        q.append(root)
        solve(q)
        return ans