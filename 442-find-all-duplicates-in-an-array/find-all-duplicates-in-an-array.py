class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # i=0
        # ans= []

        # while i < len(nums):
        #     corr=nums[i]-1

        #     if nums[i] != nums[corr]:
        #          nums[i], nums[corr] = nums[corr] , nums[i]
              
                
        #     else:
        #         i+=1
            

        # for i in range(len(nums)):
        #     if nums[i]-1 != i:
        #         ans.append(nums[i])

        # return ans




        ans = []
        l = 0

        while l < len(nums):
            corr = nums[l] - 1
            if nums[corr] == nums[l]:
                l += 1
            else:
                nums[corr],nums[l] = nums[l],nums[corr]

        for i in range(len(nums)):
            
            if i + 1 != nums[i]:
                ans.append(nums[i])
        return ans












                
        