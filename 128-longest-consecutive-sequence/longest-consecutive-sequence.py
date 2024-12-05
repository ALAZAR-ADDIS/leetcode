class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
      
        longest=0
        maxCons=0
        prev_max=float("-inf")
        for  i in range(len(nums)):
            print(prev_max)
            
            if prev_max+1==nums[i]:
                longest+=1
                prev_max=nums[i]
            elif  prev_max==nums[i]:
                pass
            
            else :
                print(prev_max+1,nums[i])
                print("The longest Has been changed",longest)
                longest=1
                prev_max=nums[i]
            
            maxCons=max(maxCons,longest)
        return maxCons
    
            


        
            


        