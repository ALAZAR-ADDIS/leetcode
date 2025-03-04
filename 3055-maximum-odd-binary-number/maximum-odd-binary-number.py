class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        One_zeros = Counter(s)
        One_zeros["1"] -= 1
       
        ans = []
        for i in range(One_zeros["1"]):
            ans.append(1)
        
        for i in range(One_zeros["0"]):
            ans.append(0)
        
        ans.append(1)
        return "".join(map(str,ans))

        
        