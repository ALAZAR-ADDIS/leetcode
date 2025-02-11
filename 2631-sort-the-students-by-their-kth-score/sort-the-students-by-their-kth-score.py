class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        # score.sort(key = lambda x :x[k])
        # return score[::-1]

        self.divide(score,0,len(score)-1,k)
        return score[::-1]

        

    def divide(self,arr,l,r,k):
        if l<r:
            mid = (l + r)//2
            self.divide(arr,l,mid,k)
            self.divide(arr,mid + 1, r,k)
            self.merge(arr,l,mid,r,k)


    def merge(self,nums,left,mid,right,k):

        
        temp = []
        l = left
        r = mid + 1
        while l <= mid or r <= right:

            if  r > right or (l <= mid and self.compare(nums[l] , nums[r],k)):
                temp.append(nums[l])
                l += 1
            
            else:
                temp.append(nums[r])
                r += 1
        for i  in range(left, right +1):
            nums[i] = temp[i - left]




    def compare(self,row1,row2,k):
   
        return row1[k] <= row2[k]
        