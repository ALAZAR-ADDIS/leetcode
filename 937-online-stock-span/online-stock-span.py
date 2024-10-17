class StockSpanner:

    def __init__(self):

        self.stack=[]
        self.counter=[]
       
        

    def next(self, price: int) -> int:
       
        count=1
        
        while self.stack and self.stack[-1]<=price:
            count+=self.counter[-1]
            self.counter.pop()
            self.stack.pop()
        self.stack.append(price)
        self.counter.append(count)
        return count
            

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)