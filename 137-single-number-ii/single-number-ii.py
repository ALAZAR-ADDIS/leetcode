class Solution:
    def singleNumber(self, nums: List[int]) -> int:


        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        
        for c in counter.keys():
            if counter[c] == 1:
                return c
        