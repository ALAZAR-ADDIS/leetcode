class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        ans = 0

        while l <= r:
            
            mid = (l + r)//2 
           
                     
            if mid*mid > x:

                r = mid -1
            else:
                # print(mid)
                # ans = mid
                l = mid +1


        return r