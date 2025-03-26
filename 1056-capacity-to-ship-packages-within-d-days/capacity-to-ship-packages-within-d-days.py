class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def daysCount(capacity):
            curr = 0
            day = 1
            for num in weights:
                if curr + num > capacity:
                    curr = num
                    day +=1
                else:
                    curr += num
            return day
        maxx = max(weights)
        summ = sum(weights)

        l = maxx
        r = summ

        while l <= r:
            mid = (l + r)//2

            if daysCount(mid) <= days:
                r = mid - 1
            else:
                l = mid + 1
        return l
            
        