class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        def Finder(target,nums):
            l = -1
            r = len(nums)

            while l + 1 < r:
                mid = (l + r)//2
                if nums[mid][0] >= target:
                    r = mid
                else: 
                    l = mid
            return nums[r] if r != len(nums) else  -1
        
        temp = sorted(intervals,key = lambda x: x[0])
        print(temp)
        ans =[]
        maped = {n[0]:i for i,n in enumerate(intervals)}
        for start,end in intervals:
            val = Finder(end,temp)
            if val == -1:
                ans.append(-1)
            else:
                ans.append(maped[val[0]])
        return ans


        