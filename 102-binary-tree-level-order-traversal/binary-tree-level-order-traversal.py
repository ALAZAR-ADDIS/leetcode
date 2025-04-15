# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


        # def helper(qu):
        #     if not qu:
        #         return 

        #     i = len(qu)
        #     temp = []
        #     nextsize = 0
       
            
        #     while i > 0 :
        #         poped = qu.popleft()
        #         temp.append(poped.val)

        #         if poped.left:
        #             qu.append(poped.left)
        #             nextsize += 1

        #         if poped.right:
        #             qu.append(poped.right)
        #             nextsize += 1
                          

        #         i -= 1

        #     ans.append(temp)
        #     helper(qu)

        # if not root:
        #     return []

        # ans =[]
        # q = deque()
        # q.append(root)
        # helper(q)

        # return ans
        if not root:
            return []
        
        qu = deque([root])
        ans = []

        while qu:
            leng = len(qu)
            temp = []

            for _ in range(leng):
                node = qu.popleft()
                temp.append(node.val)

                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
            ans.append(temp)
        return ans

        
        