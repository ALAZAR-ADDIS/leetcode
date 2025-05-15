class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:



        # def solve(path,i):
        #     if i == len(nums):
        #         ans.append(path[::])                
        #         return 

        #     path.append(nums[i])         

        #     solve(path,i + 1)

        #     path.pop()


        #     solve(path,i + 1)

        # ans = []
        # solve([],0)       

       
        # return ans

        n = len(nums)
        result = []
        for i in range(1 << n):
            res = []
            for j in range(n):
                if i & (1 << j):
                    res.append(nums[j])  
            result.append(res[:])  
        return result

          
        