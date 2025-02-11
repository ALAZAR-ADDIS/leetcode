class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str,nums))
        self.divide(nums,0,len(nums)-1)

        return str(int("".join(nums)))
    

    def divide(self,nums,left,right):
        if left < right :
            mid = (left + right)//2
            self.divide(nums,left,mid)
            self.divide(nums,mid + 1, right)
            self.merge(nums,left,mid,right)
    
    def merge(self,nums,left,mid,right):
        temp = []
        l = left
        r = mid + 1
        while l <= mid or r <= right:

            if  r > right or (l <= mid and self.compare(nums[l] , nums[r])):
                temp.append(nums[l])
                l += 1
            
            else:
                temp.append(nums[r])
                r += 1
        for i  in range(left, right +1):
            nums[i] = temp[i - left]
    
    def compare(self,num1,num2):
        return num1 + num2 >=  str(num2) + str(num1)


        