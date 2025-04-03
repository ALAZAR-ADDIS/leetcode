# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        num = set(nums)
        hd = head

        while hd:
            if hd.val in num:
                prev.next = hd.next
                hd = hd.next   
                continue                        
                
            prev = hd
            hd = hd.next   

        return dummy.next

        