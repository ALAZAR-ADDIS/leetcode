class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=nums[::]
        post=nums[::]
        for i in range(1,len(nums)):
            pre[i]*=pre[i-1]
        for i  in range(len(nums)-2,-1,-1):
            post[i]*=post[i+1]
        print(post)
        print(pre)
    
        for i in range(len(nums)):
            pr=  1 if i==0 else pre[i-1]
            pos= 1 if i==len(nums)-1  else post[i+1]
            print(pr,pos)

            nums[i]=pr*pos
        return nums

        
        
        
