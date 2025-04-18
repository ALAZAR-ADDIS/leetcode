# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        l = -1
        r = n + 1
        while l + 1 < r :
            mid = ( l + r)//2

            if guess(mid) >=0:
                l = mid
            else:
                r = mid
        return l
        