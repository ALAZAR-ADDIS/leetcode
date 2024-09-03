# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
       
        prev=None
        
        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        
        l,r=head,prev

        while r:
            temp=r.next
            r.next=l.next
            l.next=r
            r=temp
            l=l.next.next
        if l:
            l.next=None
        return head
        