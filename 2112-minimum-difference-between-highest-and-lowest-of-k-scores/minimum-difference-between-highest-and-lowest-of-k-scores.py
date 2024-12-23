class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums)==1 or len(nums)==0:
            return 0
        else :
            nums.sort()
            mine=float("inf")
            l=0
            for r in range(len(nums)):

                while r-l+1>k:
                    l+=1
                if r-l+1==k:
                    mine=min(mine,nums[r]-nums[l])
                    l+=1
            return mine
        
        