# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes=set()
        a=headA
        b=headB

        while a:
            nodes.add(a)
            a=a.next
        while b:
            if b in nodes:
                return b
            b=b.next
        return None
        