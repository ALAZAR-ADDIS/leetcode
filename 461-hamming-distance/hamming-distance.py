class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0

        for i in range(32):
            if x & 1 != y & 1:
                count += 1
            
            x >>= 1
            y >>= 1
        return count
        