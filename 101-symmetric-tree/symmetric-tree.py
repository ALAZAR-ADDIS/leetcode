# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

    
        # def solve(root1,root2):

        #     if not root1 and not root2:
        #         return True

        #     if (not root1 and root2) or (not root2 and root1):

        #         return False

        #     if root1.val != root2.val:               
        #         return False

        #     left = solve(root1.left, root2.right)
        #     right = solve(root1.right,root2.left)


        #     return left and right

        # return  solve(root.left,root.right)

        def solve(qu):
            if not qu:
                return True

            leng = len(qu)
            print(leng,"This is the leng")
            while  leng > 0:
                
                left = qu.popleft() 
                right = qu.popleft()
                
                

                if (left and not right) or (not left and right):
                    return False

                if left and right and left.val != right.val:
                    return False

                if left:
                    qu.append(left.left)
                if right:
                    qu.append(right.right)
                
                if left:
                    qu.append(left.right)
                if right:
                    qu.append(right.left) 
                
                leng -= 2
        
            return solve(qu)
        q = deque()
        q.append(root.left)
        q.append(root.right)
        return solve(q)

            
            