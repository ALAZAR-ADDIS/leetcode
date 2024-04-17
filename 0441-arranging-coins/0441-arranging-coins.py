class Solution:
    def arrangeCoins(self, n: int) -> int:
        right=n
        left=1
        while right>=left:
            mid=(right+left)//2
            total=(mid**2 +mid )/2
            if total==n:
                return mid  
            elif total<n:
                left=mid+1
            else:
                right=mid-1
        return left-1