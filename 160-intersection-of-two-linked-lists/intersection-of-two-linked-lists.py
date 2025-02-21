# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
         
        l = headA
        r = headB

        while l or r: 

            if l == r:
                return r  
            
            if not l:
                l = headB
                continue

            elif not  r:
                r = headA
            else:
                l = l.next
                r = r.next

            
            

            

            

        
        
        