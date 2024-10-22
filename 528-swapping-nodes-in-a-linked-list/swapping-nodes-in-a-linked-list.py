# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # lg=0
        # dummy=ListNode(0,head)
        # r=dummy.next
        # while r:
        #     r=r.next
        #     lg+=1
        # r,l=dummy.next,dummy
        # lg=lg-k
        
        # while lg>0:
        #     r=r.next
        #     lg-=1
        # while k>0:
        #     l=l.next
        #     k-=1
        # l.val,r.val=r.val,l.val

        # return dummy.next

        curr=head
        for i in range(k-1):
            curr=curr.next
        l=curr
        r=head
        while curr.next:
            r=r.next
            curr=curr.next
        l.val,r.val=r.val,l.val
        return head
        

        
        