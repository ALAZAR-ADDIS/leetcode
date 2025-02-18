class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pre = 1
        # ans = [ 1] * len(nums)
        # post = [1] *(len(nums) + 1)
        # for i in range(len(nums)-1 , -1, -1):
        #     post[ i ] = nums[i] * post[i + 1]
        # pre = 1
        # for i in range(len(nums)):

        #     ans[i] = (pre * post[i + 1])
        #     pre *= nums[i]
        # return ans

        pre = 1
        post = 1
        ans = [1] * (len(nums))

        for i in range(len(nums)):
            ans[i] *=  pre
            ans[len(nums) - i - 1] *= post
            post *= nums[len(nums)- 1 - i]
            pre *= nums[i]
        return ans
    
        