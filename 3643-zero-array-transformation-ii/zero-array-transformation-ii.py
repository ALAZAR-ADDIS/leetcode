class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        def validate(k):
            checkList = [0] * (len(nums) + 1)

            for i in range(k +1):
                l,r,val = queries[i]
                checkList[l] += val
                checkList[r + 1] -= val
            for  i in range(1, len(checkList)):
                checkList[i] += checkList[i - 1]
           
            for i in range(len(nums)):
                if nums[i] > checkList[i]:
                    return False
            return True
        
        l = -2
        r = len (queries)

        while l+ 1 < r:
            mid = (l + r)//2
            if validate(mid):
                r = mid
            else:
                l = mid

        return r + 1 if r != len(queries) else -1
        