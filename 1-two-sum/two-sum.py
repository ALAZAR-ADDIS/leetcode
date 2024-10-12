class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair={}

        l,r=0,len(nums)-1

        while l<=r:
            total=nums[r]+nums[l]
            if total==target and r!=l:
                return [r,l]
            
            else:
                if target-nums[l] in pair:
                    return [pair[target-nums[l]],l]
                elif target-nums[r] in pair:
                    return [pair[target-nums[r]],r]
            pair[nums[r]]=r
            pair[nums[l]]=l
            l+=1
            r-=1


        