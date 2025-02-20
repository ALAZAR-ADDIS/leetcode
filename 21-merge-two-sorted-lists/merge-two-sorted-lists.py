# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = list1
        r = list2
        dummy = ListNode(0)
        curr = dummy

        while l and r:

            if not r or  (l and l.val <= r.val):
                curr.next = l
                l = l.next
            else:
                curr.next = r
                r = r.next

            curr = curr.next
        
        if l:
            curr.next = l
        else:
            curr.next = r
        return dummy.next
                

        