class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def validator(bucket):
            counter = 1
            total = 0
            for i in range(len(nums)):
                if total + nums[i] > bucket:
                    counter += 1
                    total = nums[i]
                else:
                    total += nums[i]
            return counter > k

        l = max(nums) - 1
        r = sum(nums) + 1

        while l + 1 < r:
            mid = (l + r)//2
            if validator(mid):
                l = mid
            else:
                r = mid
        return r

