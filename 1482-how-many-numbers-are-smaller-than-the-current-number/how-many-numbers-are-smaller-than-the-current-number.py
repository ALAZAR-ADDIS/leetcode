class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # list1=[]
        # for i in range (len(nums)):
        #     count=0
        #     for j in range(len(nums)):
        #         if nums[i]>nums[j]:
        #             count+=1
        #     list1.append(count)
        # return list1
        count=[0]*101

        for i in nums:
            count[i]+=1
        for i in range(1,len(count)):
            count[i]=count[i]+count[i-1]
        ans=[0]*len(nums)
        for i in range(len(nums)):
            ans[i]=count[nums[i]-1] if nums[i] !=0 else 0
        return ans

            


        
