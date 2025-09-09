class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        cand = set(candyType)
        ans = len(cand)
        n = len(candyType)//2
        for i in range(n):
            if ans -  1  <=  0:
                return i + 1
            ans -= 1
        
        return n
        