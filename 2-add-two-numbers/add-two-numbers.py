# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        ptr = dummy
        curr1 = l1
        curr2 = l2
        rem = 0

        while curr2 or curr1  or rem:
                summ = 0
                summ += curr1.val if curr1 else 0
                summ += curr2.val if curr2 else 0

                newNode = ListNode((summ + rem) % 10)
                rem = (summ + rem) // 10

                ptr.next = newNode

                if curr1:
                    curr1 = curr1.next

                if curr2 :
                    curr2 = curr2.next
                ptr = ptr.next
        
       
            
        return dummy.next

        