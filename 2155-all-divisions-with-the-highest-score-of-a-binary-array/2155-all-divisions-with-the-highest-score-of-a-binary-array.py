class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        max=0
        count=0
        listindex=[]
        for i in range(0,len(nums)+1):
            if i==0:
                count=nums[len(nums)-1]
            elif 0<i<len(nums):
                count=(i)-nums[i-1]+(nums[len(nums)-1]-nums[i-1])
            elif i==len(nums):
                count=(i)-nums[len(nums)-1]

            if max==count:
                max=count
                listindex.append(i)
            elif max<count:
                max=count
                listindex=[]
                listindex.append(i)
        return listindex
            
            
            

       