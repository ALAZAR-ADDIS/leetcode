class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        summ = [0] * 100002
        for start,end in requests:
            summ[start] += 1
            summ[end + 1] += -1
        
        
        
        for i in range(1,len(summ)):
            summ[i] += summ[i  - 1]
        
        nums.sort(reverse = True)
        summ.sort(reverse = True)
        
        

        ans = 0
        for i in range(len(nums)):
            ans += nums[i] * summ[i]
        return ans % (10**9 + 7)

        