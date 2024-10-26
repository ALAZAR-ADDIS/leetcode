# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # l,r=list1,list2
        # newNode=ListNode(0)
        # current=newNode
        # while  l or r:

        #     if (r and l and l.val<=r.val) or (r is None):
        #         current.next=l
        #         current=l
        #         l=l.next
        #     else:
        #         current.next=r
        #         current=r
        #         r= r.next

        # return newNode.next

        new=ListNode(0)
        p=new
        r,l=list1,list2
        
        while r and l:
            if l.val<=r.val:
                p.next=l
                l=l.next
            else:
                p.next=r
                r=r.next
            p=p.next
        if r:
            p.next=r
        if l:
            p.next=l
        return new.next
            



        