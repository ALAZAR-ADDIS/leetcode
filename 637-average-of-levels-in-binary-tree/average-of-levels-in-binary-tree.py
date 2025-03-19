# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        def helper(qu):
            if not qu:
                return

            i = len(qu)
            leng = len(qu)
            total = 0

            while i > 0:
                poped = qu.popleft()
                total += poped.val

                if poped.left:
                    qu.append(poped.left)
                if poped.right:
                    qu.append(poped.right)            

                i -= 1
            ans.append(total/leng)
            helper(qu)
        qu = deque()
        qu.append(root)
        ans = []

        helper(qu)

        return ans
        