class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        right=num
        left=1
        while right>=left:
            mid=(right+left)//2
            if mid**2==num:
                return True
            elif mid**2>num:
                 right=mid-1
            else:
                 left=mid+1
               
        return False