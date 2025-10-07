class Solution:
    def numDecodings(self, s: str) -> int:
        memo = defaultdict(int)
        def dp(i):
            if i >= len(s):
                return 1
            total = 0
            if i in memo:
                return memo[i]
                
            if s[i] != "0":
                if i + 1 < len(s) and  s[i]  + s[i + 1] <= "26"   :
                    total = dp(i + 2)
                
                total +=  dp(i + 1)

            memo[i] = total
            return memo[i]
        
        return dp(0)
        
        
            
        