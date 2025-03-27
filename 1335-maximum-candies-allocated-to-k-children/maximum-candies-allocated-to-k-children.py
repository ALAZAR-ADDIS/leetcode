class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        def validator(size):
            total = 0

            for i in range(len(candies)):
               
               total += candies[i]//size
                
            return total
        
        l = 1
        r = max(candies)

     
        while l <= r:
            mid = (l + r) // 2

            if validator(mid) >= k:
                l = mid + 1

            else:
                r = mid - 1
        return 0 if r <= 0 else r
        