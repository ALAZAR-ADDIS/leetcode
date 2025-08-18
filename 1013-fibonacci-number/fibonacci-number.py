class Solution:
    def fib(self, n: int) -> int:

        def solve(i):
            if i == 0:
                return 0
            if i <= 2:
                return 1
            
            return solve(i - 1) +  solve(i - 2)
        
        return solve(n)

        