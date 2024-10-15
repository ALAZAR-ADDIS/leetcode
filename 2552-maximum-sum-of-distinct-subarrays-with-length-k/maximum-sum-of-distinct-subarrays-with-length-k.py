class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l=0
        nmb={}
        total=0
        ans=0
        for i in range(len(nums)):
            nmb[nums[i]]=nmb.get(nums[i],0)+1 
            total+=nums[i]      
                     
            while len(nmb)>k  or nmb.get(nums[i],0)>1:
                nmb[nums[l]]-=1
                if nmb[nums[l]]==0:
                    nmb.pop(nums[l])
                total-=nums[l]
                l+=1
            if (i-l+1)==k:
               ans=max(ans,total)
            

        return ans
            

        