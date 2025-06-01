class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_num1 = Counter(nums1)
        count_num2 = Counter(nums2)
        ans = []

        for i in count_num1.keys():
            if count_num1[i] == count_num2[i]:
                for _ in range(count_num1[i]):
                    ans.append(i)
            elif  count_num1[i] and  count_num2[i] and  count_num1[i] != count_num2[i]:
                for _ in range(min(count_num1[i] ,count_num2[i])):
                    ans.append(i)
        return ans
