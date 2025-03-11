class Solution:
    def trailingZeroes(self, n: int) -> int:

        def factorial(n):
            if n <= 1:
                return 1
            else:
                return n * factorial(n - 1)
        val = factorial(n)
        count = 0
        while val % 10 == 0:
            count += 1
            val //= 10
        return count
        