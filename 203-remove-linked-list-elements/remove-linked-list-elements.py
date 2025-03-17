# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # dummy = ListNode(0)
        # dummy.next = head
        # prev = dummy
        # curr = dummy.next

        # while curr:
        #     if curr.val == val:
        #         prev.next = curr.next
        #         curr = curr.next
        #         continue
        #     prev = curr
        #     curr = curr.next
        # return dummy.next

        def helper(prev,curr,val):
            if not curr:
                return 
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next
            helper(prev,curr,val)
        dummy = ListNode(0)
        dummy.next = head
        helper(dummy,dummy.next,val)

        return dummy.next
        