# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        
        l,r=None,head
        while r:
            temp=r.next
            r.next=l
            l=r
            r=temp
        count=0
        num=0
        while l:
            num+=(2**count)*l.val
            l=l.next
            count+=1
        return num
        