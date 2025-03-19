# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        def solve(q):
            if not q:
                return False
            
            leng = len(q)
            tx = False
            ty= False
           
            while leng > 0:
                poped = q.popleft()

                if poped.left:
                   q.append(poped.left)
                
                if poped.right:
                   q.append(poped.right)
                
                leng -= 1
               

                if  poped.left and poped.left.left:
                    sec = poped.left.right.val if poped.left.right else float("inf")
                    val = set([poped.left.left.val,sec])

                    if not (x in val and y in val):
                        if poped.left.left.val == x:
                            tx = True
                            
                        if poped.left.left.val == y:
                            ty = True
                        
                
                if poped.left and poped.left.right:
                    sec = poped.left.left.val if poped.left.left else float("inf")
                    val = set([sec,poped.left.right.val])
                    
                    if not (x in val and y in val):
                        if poped.left.right.val == x:
                            tx = True
                            
                        if poped.left.right.val == y:
                            ty = True
                        


                if poped.right and poped.right.right:
                    sec = poped.right.left.val if poped.right.left else float("inf")

                    val = set([sec,poped.right.right.val])
                    
                    if not (x in val and y in val):
                        if poped.right.right.val == x:
                            tx = True
                            
                        if poped.right.right.val == y:
                            ty = True
                        

                if poped.right and poped.right.left:
                    sec = poped.right.right.val if poped.right.right else float("inf")

                    val = set([poped.right.left.val,sec])
                    
                    if not (x in val and y in val):
                        if poped.right.left.val == x:
                            tx = True
                            
                        if poped.right.left.val == y:
                            ty = True
                        
            if tx and ty:
                return True                    


            return solve(q)

       
        q = deque()
        q.append(root)
        return solve(q)


        