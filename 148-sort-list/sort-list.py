# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
         #find the mid term and make mid.next None
         if head  and  head.next:
            l=head
            r=self.findMid(head)
            temp=r.next
            r.next=None
            r=temp

            lNode=self.sortList(l)
            rNode=self.sortList(r)
            return self.merg(lNode,rNode)
         return head

         







   #find the mid
    def findMid(self,head):
        slow,fast=head,head.next

        while fast and fast.next:
           slow=slow.next
           fast=fast.next.next
        return slow
    #merge
    def merg(self,l,r):
        dummy=ListNode(0)
        curr=dummy

        while l and r:
            if l.val<=r.val:
                curr.next=l
                l=l.next
            else:
                curr.next=r
                r=r.next
            curr=curr.next
        if l:
            curr.next=l
        if r:
            curr.next=r
        return dummy.next



        