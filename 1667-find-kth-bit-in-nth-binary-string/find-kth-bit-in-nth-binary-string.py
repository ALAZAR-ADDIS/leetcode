class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return self.solve(n)[k-1]

    def solve(self, n):
        if  n == 1:
            return "0"

        else:
            prev = self.solve(n-1)
            
            return prev + "1" + self.operate(prev)

    def operate(self,n):
        ans =[]
        for char in n:
            if char == "0":
                ans.append("1")
            else:
                ans.append("0")
        return "".join(ans[::-1])




        