# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lg=0
        dummy=ListNode(0,head)
        r=dummy.next
        while r:
            r=r.next
            lg+=1
        prev1,prev2=None,None
        r,l=dummy.next,dummy
        lg=lg-k
        
        while lg>0:
            prev2=r
            r=r.next
            lg-=1
        print(r.val)
        while k>0:
            prev1=l
            l=l.next
            k-=1
        l.val,r.val=r.val,l.val

        return dummy.next
        

        
        