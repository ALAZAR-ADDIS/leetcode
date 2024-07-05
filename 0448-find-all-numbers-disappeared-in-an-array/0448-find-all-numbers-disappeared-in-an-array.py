class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        index=0
        while(index<len(nums)):
            correct=nums[index]-1
            if index==correct or nums[index]==nums[correct]:
                index+=1
            else:
                nums[correct],nums[index]=nums[index],nums[correct]
        missingList=[]
        count=0
        for i in range(0,len(nums)):
            if nums[i]!=i+1:
                missingList.append(i+1)
                
        return missingList



        