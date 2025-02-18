class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0 
        dict_num = defaultdict(int)
        dict_num[0] = 1
        summ = 0

        for i in range(len(nums)):
            summ += nums[i]
            ans += dict_num[summ - goal]
            dict_num[summ]+= 1

        return ans
            
        