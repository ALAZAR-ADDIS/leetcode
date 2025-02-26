# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        ptr = dummy

        count = 0
        piv = head
        curr = head

        while piv:

            piv = piv.next
            count += 1

            if count % k == 0:
                prev = None

                while curr != piv:

                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = temp
                
                ptr.next = prev
                ptr = head
                ptr.next = None
                head = curr
        ptr.next = curr

        return dummy.next


        































        