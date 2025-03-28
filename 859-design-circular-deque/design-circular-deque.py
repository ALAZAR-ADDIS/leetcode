class MyCircularDeque:

    def __init__(self, k: int):
        self.qu = deque()
        self.k = k
        self.size = 0
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.qu.append(value)
        self.size += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.qu.appendleft(value)
        self.size += 1
        return True
        
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.qu.pop()
        self.size -= 1
        return True
        
        
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.qu.popleft()
        self.size -= 1
        return True
        
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.qu[-1]
        

    def getRear(self) -> int:

        if self.isEmpty():
            return -1
        
        return self.qu[0]
        

    def isEmpty(self) -> bool:

        if self.size == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()