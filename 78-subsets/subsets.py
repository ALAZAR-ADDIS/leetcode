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
        ans = []
        
        for i  in range((1<<len(nums))):
            temp = []
            print(i)

            for  j in range(len(nums)):
                if 1 & (i >> j ):
                    temp.append(nums[j])
            ans.append(temp)
        return ans
                    
        


          
        