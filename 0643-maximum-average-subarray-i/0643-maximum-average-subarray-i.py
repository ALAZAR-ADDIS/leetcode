class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum=0
        for i in range(k):
            sum+=nums[i]
        total=sum
        for i in range(0,len(nums)-k):
           total-=nums[i]
           total+=nums[i+k]
           if sum<total:
                sum=total
        return sum/k
