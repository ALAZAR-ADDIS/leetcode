# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def helper(qu,rev = False):
            if not qu:
                return []
            
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
            if rev:
                ans.append(temp[::-1])
                helper(q,False)
            else:
                ans.append(temp)
                helper(q,True)
            
        if not root:
            return []
        ans = []
        q = deque()
        q.append(root)

        helper(q)

        return ans

        