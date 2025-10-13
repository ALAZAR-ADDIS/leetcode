class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo = defaultdict(int)
        memo[0] =1
        for total in range(1, target + 1):
            for n in nums:
                
                memo[total] += memo[total - n]
       
        return memo[target]


       
            

        