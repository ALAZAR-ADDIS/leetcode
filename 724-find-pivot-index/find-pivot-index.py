class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = [0]*(len(nums) + 1)

        for i in range(1,len(total)):
            total[i] += nums[i - 1] + total[i - 1]
        print(total)

        for i in range(1,len(total)):
            if total[i - 1] == total[-1] - total[i]:
                return i - 1
        
        return  - 1
        