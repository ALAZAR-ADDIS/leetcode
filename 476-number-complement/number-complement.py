class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        p = 0
        while num :
            if num % 2 == 0:
                ans +=  (2** p)
            num //= 2
            p += 1
        return ans

        