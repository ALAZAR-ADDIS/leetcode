class Solution:
    def climbStairs(self, n: int) -> int:
        memo = defaultdict(int)
    
        def solve(i):
  
            if i in memo:
                return memo[i]
            
            if i == 0:
                return 1
            if i == 1:
                return 1
            
            memo[i] = solve(i - 1) + solve(i - 2) 
            return memo[i]
        
        return solve(n)
            
        