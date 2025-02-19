# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = dummy
        for i in range(n):
            curr = curr.next

        while  curr.next :
            curr = curr.next
            prev = prev.next

             
        prev.next = prev.next.next
        

        return dummy.next
    

        