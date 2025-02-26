class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # dict_count = defaultdict(int)
        # dict_count[0] = -1
        # summ = 0
        # ans = 0
        # for i in range(len(nums)):
        #     summ += 1 if nums[i] else -1
            
        #     if summ in dict_count:
        #         ans = max(ans, i - dict_count[summ])
        #     else:
        #         dict_count[summ] = i      
            

        # return ans

        ones = 0
        zeros = 0
        dict_count = defaultdict(int)
        dict_count[0] = -1
        ans = 0

        for i in range(len(nums)):
            ones += 1 if nums[i] else 0
            zeros += 0 if nums[i] else 1
            diff  = ones - zeros

            if  diff in dict_count:
                ans = max(ans, i - dict_count[diff])
            else:
                dict_count[diff] = i


        return ans

        