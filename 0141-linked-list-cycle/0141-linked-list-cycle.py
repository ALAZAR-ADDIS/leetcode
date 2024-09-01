# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # address=set()
        
        # l=head
        # while l:
           
        #    if l in address:
        #         return True
        #    address.add(l)
        #    l=l.next
        # return False

        #another approch to do this wz out any memory requirment
        slow,fast=head,head
        while fast and fast.next:
            
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                return True
        return False