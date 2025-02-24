class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        dict_count = defaultdict(int)
        dict_count[0] = -1
        summ = 0

        for i in range(len(nums)):
            summ += nums[i]

            if  (summ % k in dict_count) and (i - dict_count[summ % k] ) >=2:
                return True
                
            if summ % k not in dict_count:
                dict_count[summ % k ] = i
        return False

        