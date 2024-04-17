class Solution:
    def mySqrt(self, x: int) -> int:
        right=x
        left=0
        while right>=left:
            mid=(right+left)//2
            sqr=mid**2
            if sqr==x:
                return mid
            elif sqr<x:
                left=mid+1
            else:
                right=mid-1
        return left-1
        