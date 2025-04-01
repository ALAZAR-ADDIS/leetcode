class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def dev(l,r):
            if l < r:
                mid = (l + r)//2
                dev(l,mid)
                dev(mid + 1, r)
                merge(l,mid,r)

        def merge(l,mid, r):

            left = l
            right = mid + 1
            ans = []

            while left <= mid or right <= r:
                if  right > r or (left <= mid and nums[left] <= nums[right]):
                    ans.append(nums[left])
                    left += 1
                else:
                    ans.append(nums[right])
                    right += 1

            for i in range(l, r + 1):
                nums[i] = ans[i - l]
            
        dev(0,len(nums) -1)

        return nums






       
            
                
        