class StockSpanner:

    def __init__(self):

        self.stack=[]
        self.counter=[]
       
        

    def next(self, price: int) -> int:
        l=len(self.stack)-1
        count=1
        
        while self.stack and l>=0 and self.stack[l]<=price:
            count+=self.counter[l]
            l-=self.counter[l]
        self.stack.append(price)
        self.counter.append(count)
        return count
            

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)