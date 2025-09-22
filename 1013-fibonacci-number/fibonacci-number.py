class Solution:
    def fib(self, n: int) -> int:
        memo = defaultdict(int)
        def solve(i):
            if i == 0:
                return 0
            if i <= 2:
                return 1
            
            if i in memo:
                return memo[i]
                
            memo[i] = solve(i - 1) +  solve(i - 2)

            return memo[i]
        
        return solve(n)

        