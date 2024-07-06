class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #cycle sort algorithm
        index=0
        while index<len(nums):
            correct=nums[index]-1
            if nums[index]!=nums[correct]:
                nums[index],nums[correct]=nums[correct],nums[index]
            else:
                index+=1
        
        #find the duplicates
        duplicateList=[]
        for i in range(len(nums)):
            if nums[i]-1!=i:
                  duplicateList.append(i+1)
        return duplicateList
        



        