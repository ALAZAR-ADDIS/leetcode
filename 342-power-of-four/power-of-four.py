class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        def pow(n, num ):

            if num == n:
                return True
            elif num > n:
                return False
            powe = num * 4
            return  pow(n, powe)
        return pow(n, 1)
        