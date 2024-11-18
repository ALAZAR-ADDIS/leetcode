class Solution:
    def findLHS(self, nums: List[int]) -> int:
        maxe=-float("inf")
        mine=float("inf")
        l,r=0,0
        size=0
        nums.sort()
        while r<len(nums):
            dif=nums[r]-nums[l]
            if dif==1:
                size=max(size,r-l+1)
            if dif>1:
                l+=1
            else:
                r+=1
        return size

