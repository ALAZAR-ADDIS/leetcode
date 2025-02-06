class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count_num = Counter(nums)
        # avg=len(nums)/2

        # for i in count_num:

        #     if avg <= count_num[i]:

        #         return i



        #option 2

        # num_freq = {}
        # res = 0
        # max_freq = -float("inf")

        # for num in nums:

        #     num_freq[num] = num_freq.get(num, 0) + 1

            

        #     if max_freq < num_freq[num]:
        #         max_freq = num_freq[num]
        #         res = num
        # print(max_freq)

        # return res

        res = nums[0]
        count = 1

        for i in range(1,len(nums)):

            count += 1 if res == nums[i] else -1

            if count == 0:
                count = 1
                res = nums[i]
        
        return res
            

        
        