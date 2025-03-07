class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
       
        stack = []
        min_val = float("inf")

        for i in range(len(nums)):

            while  stack and stack[-1][0] <= nums[i]:
                stack.pop()
            
            if stack and stack[-1][1] < nums[i]:
                return True

            stack.append([nums[i],min_val])
            min_val = min(min_val , nums[i])

        return False
        
                        
        
        
    