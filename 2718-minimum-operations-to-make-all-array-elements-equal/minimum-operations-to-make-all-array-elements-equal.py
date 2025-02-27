class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
            nums.sort()

            pref = [0] * (len(nums) + 1)

            for i in range(1,len(pref)):
                pref[i] += pref[i - 1] + nums[i - 1]

        
            ans = []
            
            for num in queries:
                index = self.doBinary(num,nums)


                if index < len(nums):
                    min_op = (num*index - pref[index]) + ((pref[-1] - pref[index]) - ((len(nums) - index )* num ))
                    ans.append(min_op)
                else:
                    min_op = (num*len(nums) - pref[-1])
                    ans.append(min_op) 


            
            return ans
    
    def doBinary(self,target,nums):
        l = 0
        r = len(nums) - 1

        while l<= r:
            mid = (l + r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l
        