class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        counter = Counter(nums)
        for c in counter:
            if counter[c] == 1:
                return c
        