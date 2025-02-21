# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        l = dummy1
        r = dummy2

        curr = head

        while curr:
            temp = curr.next
            if curr.val < x:

                l.next = curr
                l = l.next
                

            else:

                r.next = curr
                r = r.next

            curr.next = None
            curr = temp

        l.next = dummy2.next
        return dummy1.next