class Node :
    def __init__(self,val,next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None
       

    def get(self, index: int) -> int:
        
        temp = self.head
        while index > 0 and  temp:
            temp = temp.next
            index -= 1
        
        
        
        if index or not temp:
            return - 1
        else:

            return temp.val
        

    def addAtHead(self, val: int) -> None:
        #checked

        dummy = Node(0)
        newNode = Node(val)
        
        newNode.next = self.head
        dummy.next = newNode
        self.head = newNode
        

        
        

    

    def addAtTail(self, val: int) -> None:
        # Checked
        dummy = Node(0)
        dummy.next = self.head
        curr = dummy
        newNode = Node(val)

        while curr.next:
            curr = curr.next
        curr.next = newNode
        self.head = dummy.next
        
        
        


    def addAtIndex(self, index: int, val: int) -> None:
        #checked
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        curr = dummy.next
        newNode= Node(val)

        while curr and index > 0:
            prev = prev.next
            curr  = curr.next
            index -= 1

        if index:
            return 
        else:
            prev.next = newNode
            newNode.next = curr
            self.head = dummy.next
        
        

    def deleteAtIndex(self, index: int) -> None:
        #checked

        dummy = Node(0)
        dummy.next = self.head

        prev = dummy
        curr = dummy.next
       

        while curr and index > 0:
            prev = prev.next
            curr  = curr.next
            index -= 1
            
        if index or not curr:
            return 
        else:
            prev.next = curr.next
            curr.next = None
            self.head = dummy.next
          


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)