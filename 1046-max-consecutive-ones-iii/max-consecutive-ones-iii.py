class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count_dict = defaultdict(int)
        l = 0
        max_len = 0 
        for r in range(len(nums)):
            count_dict[nums[r]] += 1
            while count_dict[0] > k:
                count_dict[nums[l]] -= 1
                l+=1
            max_len = max(max_len, r - l + 1)
        
        return max_len
        