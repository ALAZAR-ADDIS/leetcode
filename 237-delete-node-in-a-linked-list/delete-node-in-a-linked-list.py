# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        temp = node.next
        prev= node
        
        while  temp.next:
            prev.val = temp.val
            temp = temp.next
            prev = prev.next
        prev.val = temp.val
        prev.next = None
        