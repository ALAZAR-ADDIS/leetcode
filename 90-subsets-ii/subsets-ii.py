class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:


        def solve(path,i):
                print(path)
                if i >= len(nums):
                    ans.append(path[::])
                    return 
                
                
                
                path.append(nums[i])
                solve(path, i + 1)
                path.pop()
                

                while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                    i += 1

                solve(path, i + 1)


        ans = list()
        nums.sort()
        solve([], 0)
        return ans
            

            