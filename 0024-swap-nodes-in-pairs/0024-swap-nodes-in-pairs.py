# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode(next=head)
        prev,l=dummy,head

        while l and l.next:

           r=l.next
           nxtptr=l.next.next

           r.next=l
           l.next=nxtptr
           prev.next=r

           prev= l
           l=nxtptr

        return dummy.next

            

            
        