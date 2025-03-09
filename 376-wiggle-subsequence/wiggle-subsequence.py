class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1      

        i = 1
        val = nums[1] - nums[0]
        ans = 1

        if val > 0 or val < 0:
            ans  += 1
     

        while i < len(nums):
           
           
            if val > 0:
                
                while i < len(nums) and val >= 0 :
                    if nums[i] - nums[i - 1] < 0:
                        ans += 1
                    val = nums[i] - nums[i - 1]
                    i += 1
            elif val < 0:

                while i < len(nums) and val <= 0 :
                    if nums[i] - nums[i - 1] > 0:
                        ans += 1
                    val = nums[i] - nums[i - 1]
                    i += 1      

            else :
                
                while i < len(nums) and val == 0 :

                    if nums[i] - nums[i - 1] > 0 or nums[i] - nums[i - 1] < 0  :
                        ans += 1
                    val = nums[i] - nums[i - 1]
                    i += 1
        return ans
        