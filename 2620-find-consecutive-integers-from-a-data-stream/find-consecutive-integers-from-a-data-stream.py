class DataStream:

    def __init__(self, value: int, k: int):
        self.val=value
        self.k=k
        self.q=deque() 
        self.count=0       

    def consec(self, num: int) -> bool:
        
        self.q.append(num)
        if num==self.val:
            self.count+=1
        if len(self.q)>self.k:
            if self.q[0]==self.val:
                self.count-=1
            self.q.popleft()
        return self.k==self.count
            


        
       
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)