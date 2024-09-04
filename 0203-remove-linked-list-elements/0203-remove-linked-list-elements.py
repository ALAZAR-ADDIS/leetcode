# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        l=dummy
        r=dummy.next
        while r:
            if r.val==val:
                l.next=r.next
                r=r.next
            else:
                r=r.next
                l=l.next
        return dummy.next

        