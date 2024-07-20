class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]=nums[i-1]+nums[i]
        
        for i in range(0,len(nums)):
            if i==0:
                if nums[len(nums)-1]-nums[0]==0:
                    return 0
            else:
               if nums[i-1]==nums[len(nums)-1]-nums[i]:
                    return i
        return -1
        