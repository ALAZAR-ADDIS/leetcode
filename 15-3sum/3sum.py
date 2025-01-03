class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]

        for i,n in enumerate(nums):
            if i>0 and n==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                total=nums[r]+nums[l]+n
                if total>0:
                    r-=1
                elif total<0:
                    l+=1
                else:
                    ans.append([n,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return ans


            


        

         