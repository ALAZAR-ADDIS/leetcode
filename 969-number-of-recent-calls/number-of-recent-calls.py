class RecentCounter:

    def __init__(self):
        # self.req = deque()
        self.req = []
        self.ptr = 0
        

    def ping(self, t: int) -> int:

        while self.req and self.ptr < len(self.req) and t - self.req[ self.ptr ] > 3000:
            self.ptr +=1 

            # self.req.popleft()


        self.req.append(t)

        # return len(self.req)
        return len(self.req) - self.ptr
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)