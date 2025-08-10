class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        small = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                small = i - 1
                break
        if small == -1 :
            nums.sort()
            return 
        
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[small]:
                nums[i],nums[small]= nums[small], nums[i]
                break       
       
        
       

        temp = nums[small + 1:]
        temp.sort()

        i = -1
        print(temp, nums)
        while temp:
            
            nums[i] = temp.pop()

            i -= 1

            
