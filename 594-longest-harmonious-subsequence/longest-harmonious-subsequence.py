class Solution:
    def findLHS(self, nums: List[int]) -> int:
        maxe=-float("inf")
        mine=float("inf")
        l,r=0,0
        s=0
        nums.sort()
        while r<len(nums):
            diff=nums[r]-nums[l]
            if diff==1:
                s=max(s,r-l+1)
            if diff>1:
                l+=1
            else:
                r+=1
        return s

