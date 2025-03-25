class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l ,r = 0 , len(nums) - 1
        left,right = -1,-1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                left = mid
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        if left ==  - 1:
            return [-1, -1]

        l ,r = 0 , len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                right = mid
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return [left , right]
            