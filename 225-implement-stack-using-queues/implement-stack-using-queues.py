class MyStack:

    def __init__(self):
        self.Q=[]
        

    def push(self, x: int) -> None:
        self.Q.append(x)
        

    def pop(self) -> int:
        
        for i in range(len(self.Q)-1):
              self.Q.append(self.Q.pop(0))           
        return  self.Q.pop(0)
        

    def top(self) -> int:
        return self.Q[-1]

        

    def empty(self) -> bool:
        if self.Q:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()