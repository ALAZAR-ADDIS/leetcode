class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        #first create use the merg sort technique
        def mergsSort(nums,left,right):
            count=0
            if left<right:
                mid=(left+right)//2
                count+=mergsSort(nums,left,mid)
                count+=mergsSort(nums,mid+1,right)
                count+=merg(nums,left,mid,right)
                return count
            return 0


        def merg(nums,left,mid,right):
            count=0
            i,j=left,mid+1
            while i <= mid:
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += (j - (mid + 1))
                i += 1
           

               
            
                   
                   
            rm=mid+1
            lm=left
            temp=[]
            while rm<=right and lm<=mid:
                if nums[lm]<nums[rm]:
                    temp.append(nums[lm])
                    lm+=1
                else:
                    temp.append(nums[rm])
                    rm+=1
            while rm<=right:
                temp.append(nums[rm])
                rm+=1
            while lm<=mid:
                temp.append(nums[lm])
                lm+=1
            for i in range(left,right+1):
                nums[i]=temp[i-left]
            return count

        left=0
        right=len(nums)-1

        return mergsSort(nums,left,right)


            
            


        
        