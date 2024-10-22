# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prev=dummy
        l,r=dummy.next,dummy.next
        count=1
        while r:
            if count%2==1:
                 temp=r.next
                 r.next=prev.next
                 prev.next=r
                 l.next=temp

                 r=temp
                 l=l.next
                 prev=prev.next
            else:
                r=r.next
            count+=1
            
        return head
        