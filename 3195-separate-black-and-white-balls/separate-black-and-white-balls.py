class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0

        l = 0
        r = len(s) - 1

        while l < r:
            if s[r] == "1":
                r -= 1
            elif  s[l]== "0":
                l += 1
            else:
                ans += r - l 
                l += 1
                r-=1
        return ans

        

      
       

        