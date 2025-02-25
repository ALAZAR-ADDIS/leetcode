# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        #find the mid
        prev = head
        curr = head

        while curr and curr.next:
            prev = prev.next
            curr = curr.next.next
        
        #revence the  elems after mid

        curr = prev
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        summ = 0

        
        while prev:
            summ = max(summ ,head.val + prev.val )
            print(head.val , prev.val)
            head = head.next
            prev = prev.next

        return summ
            
        