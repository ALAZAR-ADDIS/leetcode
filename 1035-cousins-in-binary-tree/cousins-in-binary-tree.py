# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        # def solve(q):
        #     if not q:
        #         return False
            
        #     leng = len(q)
        #     tx = False
        #     ty= False
           
        #     while leng > 0:
        #         poped = q.popleft()

        #         if poped.left:
        #            q.append(poped.left)
                
        #         if poped.right:
        #            q.append(poped.right)
                
        #         leng -= 1
               

        #         if  poped.left and poped.left.left:
        #             sec = poped.left.right.val if poped.left.right else float("inf")
        #             val = set([poped.left.left.val,sec])

        #             if not (x in val and y in val):
        #                 if poped.left.left.val == x:
        #                     tx = True
                            
        #                 if poped.left.left.val == y:
        #                     ty = True
                        
                
        #         if poped.left and poped.left.right:
        #             sec = poped.left.left.val if poped.left.left else float("inf")
        #             val = set([sec,poped.left.right.val])
                    
        #             if not (x in val and y in val):
        #                 if poped.left.right.val == x:
        #                     tx = True
                            
        #                 if poped.left.right.val == y:
        #                     ty = True
                        


        #         if poped.right and poped.right.right:
        #             sec = poped.right.left.val if poped.right.left else float("inf")

        #             val = set([sec,poped.right.right.val])
                    
        #             if not (x in val and y in val):
        #                 if poped.right.right.val == x:
        #                     tx = True
                            
        #                 if poped.right.right.val == y:
        #                     ty = True
                        

        #         if poped.right and poped.right.left:
        #             sec = poped.right.right.val if poped.right.right else float("inf")

        #             val = set([poped.right.left.val,sec])
                    
        #             if not (x in val and y in val):
        #                 if poped.right.left.val == x:
        #                     tx = True
                            
        #                 if poped.right.left.val == y:
        #                     ty = True
                        
        #     if tx and ty:
        #         return True                    


        #     return solve(q)

       
        # q = deque()
        # q.append(root)
        # return solve(q)


        def solve(root,xx,yy):
            find_x = find_one(root, xx)
            find_y = find_one(root,yy)

            print((issibling(root,xx,yy)))
            

            return  (find_label(root,find_x,0) == find_label(root,find_y,0)) and not(issibling(root,find_x,find_y))
        
        def find_one(root,target):
            if not root:
                return  None
            if root.val == target:
                return root
            left = find_one(root.left,target)
            if left:
                return left
            return find_one(root.right,target)
        
        def find_label(root,n,l):
            if not root:
                return -1

           
            if root == n:
                
                return l

            left = find_label(root.left,n, l + 1)
           
            if left != -1:
                return left
            
            return find_label(root.right,n,l + 1)
        
        def issibling(root,x,y):
            if not root:
                return False
            return (root.left == x and root.right == y) or  (root.left == y and root.right == x) or (issibling(root.left,x,y) or issibling(root.right,x,y))


        return solve(root, x,y)
        