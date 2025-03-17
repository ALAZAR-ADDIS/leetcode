# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # l = list1
        # r = list2
        # dummy = ListNode(0)
        # curr = dummy

        # while l and r:

        #     if not r or  (l and l.val <= r.val):
        #         curr.next = l
        #         l = l.next
        #     else:
        #         curr.next = r
        #         r = r.next

        #     curr = curr.next
        
        # if l:
        #     curr.next = l
        # else:
        #     curr.next = r
        # return dummy.next
                

        def solve(ptr1,ptr2,curr):

            if not ptr1:
                curr.next = ptr2
                return

            if  not ptr2:
                curr.next = ptr1
                return
            
            if ptr1.val <= ptr2.val:
                curr.next = ptr1
                return solve(ptr1.next, ptr2, curr.next)
               

            else:
                curr.next = ptr2 
                solve(ptr1, ptr2.next, curr.next)
                
            

            
           
        dummy = ListNode(0)
        p1= list1
        p2= list2

        solve(p1,p2,dummy)

        return dummy.next

            
                
        