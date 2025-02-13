class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        total=0
        for i in range(k):
            total += nums[i]
        ans = total
        for i in range(len(nums)-k):
            total -= nums[i]
            total += nums[i + k]
            ans = max(total, ans)
        return ans/ k
            

        