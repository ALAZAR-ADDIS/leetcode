class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        val = int(sqrt(c))
        l = 0
        r= val + 1

        while l <= r:
            sqr = l**2 + r**2
            if sqr == c:
                return True
            elif sqr > c:
                r -= 1
            else:
                l += 1
                
        return False
        