class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        ans=[-1 for i in range(len(nums))]
        for i,n in enumerate(nums):

            while stack and nums[stack[-1]]<n:
                ans[stack[-1]]=n
                stack.pop()
            stack.append(i)
        print(ans,stack)
        
        for n in nums:
            while stack and nums[stack[-1]]<n:
                ans[stack[-1]]=n
                stack.pop()
        return ans
        