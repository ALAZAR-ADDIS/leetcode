class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        ans = float("inf")
        pref = [0] * (len(nums) + 1)
        nums.sort()
        

        for i in range(1,len(pref)):
            pref[i] += pref[i - 1] + nums[i - 1]
        
        for i in range(1,len(pref)):
            pre = nums[i-1] * (i-1) - pref[i - 1]
            post = pref[-1] - pref[i - 1] - (nums[i - 1] *(len(pref) - i))

            ans = min(ans , pre + post)

        return ans
        

        