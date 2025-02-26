# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyOdd = ListNode(0)
        dummyEven = ListNode(0)

        odd = dummyOdd
        even = dummyEven

        curr = head
        is_odd = True

        while curr:
            if is_odd:
                odd.next = curr
                odd = odd.next
                is_odd = False
            else:
                even.next = curr
                even = even.next             
                is_odd = True
                
            temp = curr.next
            curr.next = None
            curr = temp
       
        
        odd.next = dummyEven.next

        return dummyOdd.next

        