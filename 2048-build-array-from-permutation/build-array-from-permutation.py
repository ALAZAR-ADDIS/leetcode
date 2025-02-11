class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        # ans = [0]*len(nums)

        # for i in range(len(nums)):

        #     ans[i]=nums[nums[i]]
        
        # return ans
        
        for i in range(len(nums)):
            val = nums[i]  % len(nums)
            nums[i] = (nums[val] % len(nums)) * len(nums) + val
        
        for i in range(len(nums)):
            nums[i] //= len(nums)
        
        return nums