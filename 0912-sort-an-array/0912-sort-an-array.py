class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergSort(nums,left,right):
            if left<right:
                mid=(right+left)//2
                mergSort(nums,left,mid)
                mergSort(nums,mid+1,right)
                merg(nums,left,mid,right)
            
        def merg(nums,left,mid,right):
            lm=left
            rm=mid+1
            temp=[]
            while lm<=mid and rm<=right:
                if nums[lm]<nums[rm]:
                    temp.append(nums[lm])
                    lm+=1
                else:
                    temp.append(nums[rm])
                    rm+=1
            while lm<=mid:
                 temp.append(nums[lm])
                 lm+=1
            while rm<=right:
                temp.append(nums[rm])
                rm+=1
            for i in range(left,right+1):
                nums[i]=temp[i-left]
            
        mergSort(nums,0,len(nums)-1)
        return nums        

        