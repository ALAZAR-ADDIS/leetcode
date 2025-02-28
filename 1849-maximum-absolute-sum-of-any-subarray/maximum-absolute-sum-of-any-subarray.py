class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxx = 0
        minn = 0

        total = 0

        for i in range(len(nums)):
            total += nums[i]

            if total > 0:
                maxx = max(maxx , total)
            
            else:
                total = 0

        total = 0
        
        for i in range(len(nums)):
            total += nums[i]

            if total < 0:
                minn = min(minn , total)
            else:
                total = 0

        # if minn == float("inf"):
        #     return abs(maxx)
        # elif maxx == -float("inf"):
        #     return abs(min)
        # else:          
        return max(abs(maxx),abs(minn))


            


    





        