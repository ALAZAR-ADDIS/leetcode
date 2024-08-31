class ListNode:
    def __init__(self,val,next=None,prev=None):
        self.val=val
        self.next=next
        self.prev=prev



class MyLinkedList:

    def __init__(self):
        self.right=ListNode(0)
        self.left=ListNode(0)
        self.left.next=self.right
        self.right.prev=self.left
     
        

    def get(self, index: int) -> int:
        curr=self.left.next
       
        while curr and index>0 :
            index-=1
            curr=curr.next
        if curr and curr!=self.right and index==0 :
            return curr.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        newNode=ListNode(val)
        newNode.next=self.left.next
        newNode.prev=self.left
        
        self.left.next.prev=newNode
        self.left.next=newNode

        

    def addAtTail(self, val: int) -> None:
        newNode=ListNode(val)
        newNode.prev=self.right.prev
        newNode.next=self.right
        
        self.right.prev.next=newNode
        self.right.prev=newNode
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr=self.left.next
        newNode=ListNode(val)
        while curr and index>0:
            index-=1
            curr=curr.next
        if curr   and index==0  :
            newNode.next=curr
            newNode.prev=curr.prev

            curr.prev.next=newNode
            curr.prev=newNode

        

    def deleteAtIndex(self, index: int) -> None:
        curr=self.left.next
        while curr and index>0:
            index-=1
            curr=curr.next
        if curr and curr!=self.right  and index==0 :
            curr.prev.next=curr.next
            curr.next.prev=curr.prev

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)