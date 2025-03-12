class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return self.solve(n)[k-1]

    def solve(self, n ,prev = "0"):
        if  n - 1 == 0:
            return prev

        else:
            prev = prev + "1"  + self.operate(prev)
            return self.solve(n-1 , prev)

    def operate(self,n):
        ans =[]
        for char in n:
            if char == "0":
                ans.append("1")
            else:
                ans.append("0")
        return "".join(ans[::-1])




        