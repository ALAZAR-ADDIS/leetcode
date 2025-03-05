class RecentCounter:

    def __init__(self):
        self.req = deque()
        

    def ping(self, t: int) -> int:

        while self.req and t - self.req[0] > 3000:
            self.req.popleft()
            
        self.req.append(t)

        return len(self.req)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)