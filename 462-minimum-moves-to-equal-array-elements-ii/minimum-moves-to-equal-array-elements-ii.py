class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # ans = float("inf")
        # pref = [0] * (len(nums) + 1)
        # summ = sum(nums)
        # nums.sort()
        
        

        # for i in range(1,len(pref)):
        #     pref[i] += pref[i - 1] + nums[i - 1]
        
        # for i in range(1,len(pref)):
        #     pre = nums[i-1] * (i-1) - pref[i - 1]
        #     post = summ - pref[i - 1] - (nums[i - 1] *(len(pref) - i))

        #     ans = min(ans , pre + post)

        # return ans
        nums.sort()
        mid = len(nums)//2
        target = nums[mid]

        
        return sum([abs(target - n) for n in nums])

        