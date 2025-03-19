# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        def solve(p):
            if not p:
                return 
            
            leng = len(p)
            maxx= -float("inf")

            while  leng > 0:

                poped = p.popleft()
                maxx = max(maxx, poped.val)

                if poped.left:
                    p.append(poped.left)

                if poped.right:
                    p.append(poped.right)
                leng -= 1
            ans.append(maxx)
            solve(p)
        if not root:
            return []
        
        q= deque()
        q.append(root)
        ans = []
        solve(q)


        return ans
        