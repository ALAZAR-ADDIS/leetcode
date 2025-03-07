class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:

        """

        general idea is to find the  PSE NSE

        """

        # prev smaller

        stack = []
        PSE = [-1] * len(nums)

        for i in range(len(nums)):
            while stack and nums[stack[-1]] >= nums[i]:
                index = stack.pop()

            if stack:
                PSE[i] = stack[-1]
            stack.append(i)
        
        stack = []
        NSE = [len(nums)] * len(nums)


        for i in range(len(nums)):
           
            while stack and nums[stack[-1]] >= nums[i]:
                index = stack.pop()
                
                NSE[index] = i
          
            stack.append(i)
    
        ans = 0
        print(PSE ,NSE)

        for i in range(len(nums)):
            left = i - PSE[i]
            right = NSE[i] - i
            ans = (ans + left*right * nums[i]) %(10**9 + 7)
        return ans




        
        