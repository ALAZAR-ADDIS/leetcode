# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self,node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # l=node
        # r=node.next
        # while r.next:
        #     l.val=r.val
        #     r=r.next
        #     l=l.next
        # l.val=r.val
        # l.next=None
        l=node
        r=node.next
        l.val=r.val
        l.next=r.next
        
        
        
        