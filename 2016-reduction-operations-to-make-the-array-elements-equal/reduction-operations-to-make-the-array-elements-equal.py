class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count=0
        nums.sort()
        l=len(nums)-2
        while l>=0:
            
            if   nums[l]!=nums[l+1]:
                   
                    count+=len(nums)-(l+1)
            l-=1
            
            
            
        return count

        