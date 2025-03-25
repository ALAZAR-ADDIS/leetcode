# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        
        def solve(q,lev):
            if not q:
                return 
            
            leng = len(q)

            l = 0
            r = leng - 1
            if lev % 2:
                print(lev,q[-1].val)
                
                while l < r :

                    q[l].val , q[r].val = q[r].val,q[l].val
                    l +=1
                    r -= 1
            
            while leng > 0:

                poped = q.popleft()

                if poped.left:
                    q.append(poped.left)
                if poped.right:
                    q.append(poped.right)
                leng -= 1
            solve(q,lev + 1)
        q = deque()
        q.append(root)
        solve(q,0)

        return root
                