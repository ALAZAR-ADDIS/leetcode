class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
            if count[i] == n:
                return i
        