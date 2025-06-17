class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # l ,r = 0 , len(nums) - 1
        # left,right = -1,-1
        # while l <= r:
        #     mid = (l + r)//2
        #     if nums[mid] == target:
        #         left = mid
        #         r = mid - 1
        #     elif nums[mid] > target:
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        # if left ==  - 1:
        #     return [-1, -1]

        # l ,r = 0 , len(nums) - 1
        # while l <= r:
        #     mid = (l + r)//2
        #     if nums[mid] == target:
        #         right = mid
        #         l = mid + 1
        #     elif nums[mid] > target:
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        # return [left , right]
        
        l = -1
        r = len(nums)

        while l + 1 < r:
            mid = (l + r)//2
            if nums[mid] <= target:
                l = mid
            else: 
                r = mid
        
        if l < 0 or nums[l] != target:
            return [-1, -1]
        
        l2 = -1
        r2 = len(nums)

        while l2 + 1 < r2:
            mid = (l2 + r2)//2

            if nums[mid] >= target:
                r2 = mid
            else :
                l2 = mid
        return [r2,l]
