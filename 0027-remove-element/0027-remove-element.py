class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        leftpointer=0
        rightpointer=len(nums)-1
        while rightpointer>=leftpointer:
            if nums[leftpointer]==val:
                nums.pop(leftpointer)
                rightpointer-=1
            elif nums[rightpointer]==val:
                nums.pop(rightpointer)
                rightpointer-=1
            else:
                rightpointer-=1
                leftpointer+=1
        return len(nums)