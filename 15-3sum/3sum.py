class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        nums.sort()
        ans = []

        for index,val in enumerate(nums):
                if index > 0 and nums[index - 1] == nums[index]:
                    continue
                l,r = index + 1,len(nums)-1

                while l < r:

                    summ = val + nums[l] + nums[r]
                    

                    if summ == 0:
                        ans.append([val,nums[l],nums[r]])
                        l+= 1
                        r -= 1
                        
                        while r > l and nums[l] == nums[ l - 1]:
                            l += 1
                    elif summ > 0:
                        r -= 1
                    else:
                        l += 1
                        
        return ans



        