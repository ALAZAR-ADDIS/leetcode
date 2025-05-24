class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        x = 0
        for i in range(n):
            x ^= (2* i + start) 
        return x