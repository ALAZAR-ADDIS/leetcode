class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        index=0 
        while index<len(nums):
            correct=nums[index]-1
            if nums[index]!=nums[correct]:
                nums[index],nums[correct]=nums[correct],nums[index]
            else:
                index+=1
        
        MismatchList=[]
        for i in range (len(nums)):
            if nums[i]-1!=i:
                MismatchList.append(nums[i])
                MismatchList.append(i+1)
                return MismatchList