# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0 :
            return
        if len(lists)==1:
            return lists[0]
        # dummy=ListNode(0)
        # curr=dummy
        # l=lists[0]
        
        # for i in range(1,len(lists)):
        #     r=lists[i]
            
        #     while r or l:
        #         if (r and l and r.val>=l.val)  or r==None:
        #             curr.next=l
        #             l=l.next
        #         else:
        #             curr.next=r
        #             r=r.next
        #         curr=curr.next

          
        

        #     l=dummy.next
        #     curr=dummy
        # return dummy.next

        #approch 2

        while len(lists)>1:

            merged=[]

            for i in range(0,len(lists),2):
                    list1=lists[i]
                    list2=lists[i+1] if i+1<len(lists) else None
                    merged.append(self.mergList(list1,list2))

            lists=merged
        return lists[0]
    def mergList(self,l,r):
        dummy=ListNode(0)
        curr=dummy
        while l and r:
            
            if l.val<r.val:
                curr.next=l
                l=l.next
            else:
                curr.next=r
                r=r.next
            curr=curr.next
        if l:
            curr.next=l
        if r:
            curr.next=r
        return dummy.next
        
        
                    



        