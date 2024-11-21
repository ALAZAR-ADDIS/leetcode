class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        r=int(sqrt(c))+1
        l=0
        while l<=r:
            total=l**2+r**2
            if total==c:
                return True
            elif total>c:
                r-=1
            else:
                l+=1
        return False
            

        