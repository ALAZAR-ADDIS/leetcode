class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_set = set(nums1)
        ans = []

        for num in  nums2:
            if num in num1_set:
                  ans.append(num)
        return list(set(ans))

        