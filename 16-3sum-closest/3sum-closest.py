class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        prev = float("inf")
        nums.sort()
        ans = 0

        for  index,val in enumerate(nums):
            l, r = index + 1 ,len(nums) - 1

            while l < r:
                summ = val + nums[l] + nums[r]

                if summ == target:
                    return summ
                elif summ > target:
                     r -= 1
                else:
                    l += 1
                if prev > abs(target - summ):
                    prev = abs(target - summ)
                    ans = summ
            
                
            

        return ans

            
            
        