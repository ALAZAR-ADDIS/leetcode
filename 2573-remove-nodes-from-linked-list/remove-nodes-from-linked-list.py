# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
    
        def solve(curr):
            if  not curr.next:
                return curr
            
            
            
            send = solve(curr.next)
            
            curr.next = None
            
            if curr.val >= send.val:
                curr.next = send
                return curr
            else:
                return send

        dummy = ListNode(float("inf"))
        dummy.next  = head
        

        solve(dummy)
        return dummy.next
        