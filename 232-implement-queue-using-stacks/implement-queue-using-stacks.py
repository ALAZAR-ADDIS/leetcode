class MyQueue:

    def __init__(self):
        self.data=deque()
        

    def push(self, x: int) -> None:
        self.data.append(x)
        

    def pop(self) -> int:
        val=None
        if self.data:
           val=self.data.popleft()
        return val
            
        

    def peek(self) -> int:
        return self.data[0] if self.data else None

        

    def empty(self) -> bool:
        return True if len(self.data)==0 else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()