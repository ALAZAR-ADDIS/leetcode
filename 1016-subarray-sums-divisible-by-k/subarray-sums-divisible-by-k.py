class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0 
        count = defaultdict(int)
        count[0] = 1
        summ = 0
        
        for i in range(len(nums)):
            summ += nums[i]
            
            ans += count[summ % k]
            count[summ % k] += 1
        
        return ans
        