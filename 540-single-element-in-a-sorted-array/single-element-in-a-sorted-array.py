class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        l = -1
        r = len(nums)

        while l + 1 < r:
            mid = (l + r)//2

            if mid % 2:
                if nums[mid - 1] == nums[mid]:
                    l = mid
                else:
                    r = mid
            else:
                if  mid + 1 < len(nums) and nums[mid + 1] == nums[mid]:
                     l = mid
                else:
                     r = mid
        return nums[r]
