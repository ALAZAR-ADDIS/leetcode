class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        ans=list(set(nums))
        ans.sort()

        
        return max(nums) if len(ans)<3 else ans[len(ans)-3]
            

        