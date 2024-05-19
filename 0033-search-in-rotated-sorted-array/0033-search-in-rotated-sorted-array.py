class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right=len(nums)-1
        left=0
        while right>=left:
            mid=(right + left)//2
            if nums[mid]==target:
                return mid
            elif nums[left]<nums[mid]:
                if nums[left]<= target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            elif nums[left]>nums[mid]:
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                left+=1
        return -1
            