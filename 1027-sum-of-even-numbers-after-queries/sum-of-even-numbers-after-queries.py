class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        
        ans=[]
        total_even=0

        for num in nums:
            if  not num % 2:
                total_even += num

        for val,index in queries:

            new_sum = nums[index] + val

            if  not  new_sum % 2:     

                if nums[index] % 2:
                    total_even += new_sum
                    
                else:
                    total_even += val
            else:

                if not nums[index] % 2:
                    total_even -= nums[index]

            ans.append(total_even)
            nums[index] += val

        return ans
                   
                    
               

               
        