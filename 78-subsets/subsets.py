class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:



        def solve(path,i):
            if i == len(nums):
                ans.append(path[::])                
                return 

            path.append(nums[i])         

            solve(path,i + 1)

            path.pop()


            solve(path,i + 1)

        ans = []
        solve([],0)       

       
        return ans
          
        