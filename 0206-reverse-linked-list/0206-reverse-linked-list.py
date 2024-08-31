# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        right=head
        left=None
        
        while right:
            head=right.next
            right.next=left
            left=right
            right=head
        return left
            
            
        
        