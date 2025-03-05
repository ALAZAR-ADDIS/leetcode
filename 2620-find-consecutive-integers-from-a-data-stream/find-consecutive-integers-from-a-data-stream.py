class DataStream:

    def __init__(self, value: int, k: int):
        self.que = deque()
        self.count = 0
        self.k = k
        self.value = value
        

    def consec(self, num: int) -> bool:
        self.que.append(num)

        if self.value == num:
            self.count += 1

        if len(self.que) > self.k:
           
            if self.que.popleft() == self.value:
                self.count  -= 1

        return self.count == self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)