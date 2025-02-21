class ProductOfNumbers:

    def __init__(self):
        self.nums = [1,]
        self.last = 0
        

    def add(self, num: int) -> None:
        if num:
            if self.nums[-1]:
                self.nums.append(self.nums[-1] * num)
            else:
                self.nums.append(num)
            if self.last:
                self.last += 1
        else:
            self.nums.append(num)
            self.last = 1
        

    def getProduct(self, k: int) -> int:

        if self.last and k >= self.last:
            return 0
        else:
            
            if self.nums[-(k + 1)]:
                return self.nums[-1]//self.nums[- (k + 1)]
            else:
                return self.nums[-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)