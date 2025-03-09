class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # jamp_zero = True
        # index = 0

        # if len(nums) == 1:
        #     return True

        # for i in range(len(nums) - 2 , -1 , -1):

        #     if  not nums[i]  and jamp_zero:
        #         jamp_zero = False
        #         index = i            
        #     else:
        #         if nums[i] + i > index:
        #             index = 0
        #             jamp_zero = True

        # return jamp_zero

        last = len(nums)-1

        for i in range(len(nums)-2 , -1 ,-1):
            if nums[i] + i >= last:
                last = i
        return last == 0


       

        