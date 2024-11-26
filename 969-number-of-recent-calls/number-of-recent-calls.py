class RecentCounter:

    def __init__(self):
        self.RecentCounter=Deque()
        

    def ping(self, t: int) -> int:
        self.RecentCounter.append(t)
        while self.RecentCounter[0]<t-3000:
            self.RecentCounter.popleft()
        return len(self.RecentCounter)
         
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)