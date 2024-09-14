class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sum=0
        min=float("inf")

        for i in range(0,len(nums)):
            sum+=nums[i]
            if sum<min:
                min=sum
        
        
        if min<0:
            print(min)
            return (-min)+1
        return 1


        