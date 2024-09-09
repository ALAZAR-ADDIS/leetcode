# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head is None or head.next is None: return head
        
        # l,r=head,head.next
        # while r:
            
        #     while r and r.val==l.val:
        #         l.next=r.next
        #         r=r.next 
        #     if r:
        #         r=r.next
        #         l=l.next
        # return head
       
        #approch 2
        # curr=head
        # while curr and curr.next:
        #     if  curr.val == curr.next.val:
        #         curr.next=curr.next.next
        #     else:
        #         curr=curr.next
        # return head
          #approch 3
        curr=head
        while curr:
            while curr.next and curr.val==curr.next.val:
                curr.next=curr.next.next
            curr=curr.next
        return head