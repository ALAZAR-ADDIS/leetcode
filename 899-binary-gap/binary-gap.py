class Solution:
    def binaryGap(self, n: int) -> int:
        bine = bin(n)[2:]
        ans = 0
        dis = 0

        for i in  bine:
            
            if i == "1":
                ans = max(ans , dis)
                dis = 0
            dis += 1
        return ans
        