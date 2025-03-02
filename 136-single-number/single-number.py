class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        vals = Counter(nums)

        for key in vals:
            if vals[key] == 1:
                return key
                
        