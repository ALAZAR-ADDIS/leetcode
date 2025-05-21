class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        x = 0

        if len(nums1)%2:
            for num in nums2:
                x ^= num
        if len(nums2)%2:
            for num in nums1:
                x ^= num
        return x
        