class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict_nums = defaultdict(int)
        dict_nums[0] = 1
        summ = 0
        ans = 0
        for i in range(len(nums)):            
            summ += nums[i]
            ans += dict_nums[ summ - k]           

            dict_nums[summ] += 1

            
        return ans 