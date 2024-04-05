class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        leftpointer=0
        '''
        count=0
        while leftpointer<rightpointer:
           
            if nums[leftpointer]==0:
                nums.append(nums[leftpointer])
                nums.pop(leftpointer)
                rightpointer-=1
            else:
                 leftpointer+=1'''
        for rightpointer in range(len(nums)):
            if nums[rightpointer]:
                nums[leftpointer],nums[rightpointer]=nums[rightpointer],nums[leftpointer]
                leftpointer+=1

                
            
