class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        
        def check(rate):
            h = 0
            for num in piles:
              
                 h += num//rate + (1 if num % rate else 0)

                # while temp > 0:
                #     h += 1
                #     temp -= rate
            return h



        total = sum(piles)
        l = 1
        r = total

        

        while l <= r:
            mid = (l + r) // 2
            if check(mid) <= h:
                r = mid - 1
            else:
                l = mid + 1
        return l
        