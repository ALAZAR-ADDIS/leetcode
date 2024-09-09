class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ''' #approch 1
        index=0
        while index<len(nums):
            correct=nums[index]-1
            if nums[index]!=nums[correct]:
                nums[index],nums[correct]=nums[correct],nums[index]
            else:
                if index!=correct :
                    return nums[correct]
                index+=1'''
        # index=0
        # while index<len(nums):
        #     correct=nums[index]-1
        #     if index!=correct:
        #         if nums[index]!=nums[correct]:
        #             nums[index],nums[correct]=nums[correct],nums[index]
        #         else:
        #             return nums[index]
        #     else:
        #         index+=1

        #approch 2

        l=0
        while l<len(nums):
            corr=nums[l]-1
            if nums[l]!=nums[corr]:
                nums[l],nums[corr]=nums[corr],nums[l]
            else:
                l+=1
        for i in range(len(nums)):
            if i+1!=nums[i]:
                return nums[i]
       
        