# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next =  head
        prev = dummy
        curr = dummy.next

        while  curr and curr.next:
            curr = curr.next.next
            prev  = prev.next
        
        return prev.next
        