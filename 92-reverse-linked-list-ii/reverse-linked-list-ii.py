# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
       
        dummy=ListNode(0,head)
        l=dummy
        for i in range(1,left):
            l=l.next
        
        prev=None
        curr=l.next
        

        for i in range(right-left+1):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        l.next.next=curr
        l.next=prev
        return dummy.next
        