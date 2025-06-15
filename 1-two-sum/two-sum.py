
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # num_index_pair={}

        # l,r=0,len(nums)-1

        # while l <= r:

        #     if nums[l] + nums[r] ==target and l!=r:

        #         return [l,r]

        #     elif num_index_pair.get( target - nums[l] , -1 ) != -1 : 

        #         index=num_index_pair.get(target - nums[l] , -1 )
        #         return [index,l]


        #     elif num_index_pair.get( target - nums[r] , -1 ) != -1 :

        #         index=num_index_pair.get(target - nums[r] , -1 )
        #         return [index,r]
            
        #     else:
        #         num_index_pair[nums[l]]=l
        #         num_index_pair[nums[r]]=r

                
        #     l+=1
        #     r-=1

        #approac 2
         
        num_index={}
        for i in range(len(nums)):
            if num_index.get(target-nums[i],-1)!=-1:
               return [i,num_index[target-nums[i]]]
            num_index[nums[i]] = i
        
        