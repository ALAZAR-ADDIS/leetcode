# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head
        
        l,r=head,head.next
        while r:
            
            while r and r.val==l.val:
                l.next=r.next
                r=r.next 
            if r:
                r=r.next
                l=l.next
        return head