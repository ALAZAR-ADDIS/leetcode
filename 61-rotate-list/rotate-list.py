# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        
        tail=head
        length=0
        while tail.next:
            tail=tail.next
            length+=1
        length+=1

        k%=length
        if not k:
            return head

        tail.next=head
        start=head

        for i in range(length-k-1):
            start=start.next
        temp=start.next
        start.next=None
        
        return temp


        
        
        