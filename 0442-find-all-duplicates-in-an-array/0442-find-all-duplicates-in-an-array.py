class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        #cycle sort algorithm
        index=0
        while index<len(nums):
            correct=nums[index]-1
            if nums[correct]!=nums[index]:
                nums[correct],nums[index]=nums[index],nums[correct]
            else:
                index+=1

        duplicateList=[]
        for i in range(len(nums)):
            if nums[i]-1!=i:
                duplicateList.append(nums[i])
        return duplicateList

       