class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        bdict={1:0,0:0}
        maxcon=-1
        l=0
        for r in range(len(nums)):
            bdict[nums[r]]+=1
            while bdict[0]>k:
                bdict[nums[l]]-=1
                l+=1
            maxcon=max(bdict[0]+bdict[1],maxcon)
        return maxcon
            