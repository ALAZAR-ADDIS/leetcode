class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * (max(nums ) +1)

        for  num in nums:
            count[num] += 1

        for i in range(1,len(count)):
            count[i] += count[i -1]
        
        ans = []
        for num in nums:
            if num > 0:
                     ans.append(count[num -1])
            else:                
                ans.append(0)
        
        return ans
        