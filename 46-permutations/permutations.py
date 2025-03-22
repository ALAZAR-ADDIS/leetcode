class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # def helper(path,added:set):
        #     if len(path) == len(nums):
        #         ans.append(path[::])
        #         return
            

        #     for i in range(len(nums)):

        #         if nums[i] not in added:
        #             path.append(nums[i])
        #             added.add(nums[i])

        #             helper(path, added)

        #             path.pop()
        #             added.remove(nums[i])
     

        def solve(i,nums):
           
            if i == len(nums):
                print(nums)
                ans.append(nums[::])
                return
            
            for j in range(i,len(nums)):
                nums[i] ,nums[j] = nums[j] ,nums[i]

                solve(i + 1,nums)

                nums[i] ,nums[j] = nums[j] ,nums[i]
                


        ans = []
        solve(0,nums)

        return ans