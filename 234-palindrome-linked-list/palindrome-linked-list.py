# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        #find  the middle
        f = head
        s = head

        while f and f.next:

            f = f.next.next
            s = s.next
        
        #reverce the liked list

        prev = None
        curr  = s

        while curr :
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        #check
        l = head
        r = prev

        while  l and r :
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True
        