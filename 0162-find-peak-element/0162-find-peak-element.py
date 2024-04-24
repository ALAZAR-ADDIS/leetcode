class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left=1
        right=len(nums)-2
        if len(nums)>1:
            if nums[0]>nums[1]:
                return 0
            elif nums[len(nums)-1]>nums[right]:
                return len(nums)-1
        else:
            return 0

            
        while right>=left:
            mid=(right+left)//2
            if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                    return mid
            elif nums[mid]<nums[mid+1] and nums[mid]>nums[mid-1]:
                left=mid+1
            else:
                right=mid-1         
       

