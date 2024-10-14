class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r=0,len(nums)-1
        num=[0 for i in range(len(nums))]

        for i in range(len(nums)-1,-1,-1):
            if abs(nums[l])>abs(nums[r]):
                num[i]=(nums[l]**2)
                l+=1
            else:
                num[i]=(nums[r]**2)
                r-=1

        return num


       #cycle sort using map
       #make a map
       #find max  and min
       #for min ,max+l

        