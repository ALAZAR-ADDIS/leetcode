# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.root = None
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def pos(root,val):
            if not root:
                new = TreeNode(val)
                return new
            
            if root.val < val:
                root.right = pos(root.right,val)  
            else:
                root.left = pos(root.left,val)            

            return root

        def divide(left, right):
            if left > right:  
                return 
            
            mid = (left + right) // 2
            self.root = pos(self.root,listt[mid])

            divide(left, mid - 1)
            divide(mid + 1 , right)

        curr = head
        listt = []

        while curr :
            listt.append(curr.val)
            curr = curr.next

        divide(0, len(listt) - 1)
        return self.root  
        
        
        


        

        