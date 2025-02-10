class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        max_num = max(arr1)
        count_num = [0] * (max_num + 1)
        ans = []

        for i in arr1:
            count_num[i] += 1
        
        for val in arr2:
            for i in range(count_num[val]):
                ans.append(val)
                count_num[val]-=1
        
        for index, val in enumerate(count_num):
            for i in range(val):
                ans.append(index)
        return ans

        