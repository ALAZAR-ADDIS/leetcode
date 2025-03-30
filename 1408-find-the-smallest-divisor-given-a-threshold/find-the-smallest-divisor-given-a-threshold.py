class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def validator(div):
            count = 0
            for num in nums:
                val = num//div 
                if val * div == num:
                    count += val
                else:
                    count += val + 1
            
            return count > threshold
        
        l = 0
        r = sum(nums) + 1

        while l+ 1 < r:

            mid = (l  + r )//2
            if validator(mid):
                l = mid
            else:
                r = mid
        return r
