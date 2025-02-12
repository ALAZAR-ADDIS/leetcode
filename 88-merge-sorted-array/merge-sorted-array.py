class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = []
        l = 0
        r = 0


        while l < m or r < n:

            if r >= n or (l< m  and nums1[l] <= nums2[r]):
                temp.append(nums1[l])
                l += 1
            else:
                temp.append(nums2[r])
                r  += 1
        print(nums1)
        print(temp)
        for i in range(len(temp)):
            nums1[i] = temp[i]

        