# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        s = dummy
        f = dummy

        while f and f.next:

            f = f.next.next
            s = s.next
                       
            if s == f:
                s = dummy

                while f != s:
                    f = f.next
                    s = s.next
                return s
            
        return None
        

         

        