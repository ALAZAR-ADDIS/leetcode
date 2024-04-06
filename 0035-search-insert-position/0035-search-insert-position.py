class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        '''while True:
            mid=(rightbound+leftbound)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                rightbound=mid-1
                if leftbound>rightbound:
                    if nums[mid]>target:
                        return mid
                    return mid+1

            else:
                leftbound=mid+1
                if leftbound>rightbound:
                    return mid+1'''
        rightbound=len(nums)-1
        leftbound=0
        while True:
            mid=(rightbound+leftbound)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                rightbound=mid-1
            else:
                leftbound=mid+1

            if leftbound==len(nums):
                return len(nums)
            elif rightbound<leftbound:
                return rightbound+1       
        
        