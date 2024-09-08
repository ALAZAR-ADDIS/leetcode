"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldTonew={None:None}
        curr=head
        while curr:
            new=Node(curr.val)
            oldTonew[curr]=new
            new=new.next
            curr=curr.next
        curr=head
        while curr:
            oldTonew[curr].next=oldTonew[curr.next]
            oldTonew[curr].random=oldTonew[curr.random]
            curr=curr.next
        return oldTonew[head]
        