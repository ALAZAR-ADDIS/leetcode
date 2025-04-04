class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:  

        def validator(val):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= val:                   
                    count += 1
                    i += 1
                i += 1
                
            
            print(val , count)
           
            return count >= k

         
        

        l = 0
        r = max(nums)   

        while l + 1 <  r:

            mid = (r + l)//2

            if validator(mid):
                r = mid 
            else:
                l = mid 
              
     
        return r

        