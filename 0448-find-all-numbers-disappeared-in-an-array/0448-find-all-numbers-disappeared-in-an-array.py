class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        index=0
        while(index<len(nums)):
            correct=nums[index]-1
            if  nums[index]!=nums[correct]:
                nums[correct],nums[index]=nums[index],nums[correct]
            else:
                  index+=1
                
        missingList=[]
        count=0
        for i in range(0,len(nums)):
            if nums[i]!=i+1:
                missingList.append(i+1)
                
        return missingList



        