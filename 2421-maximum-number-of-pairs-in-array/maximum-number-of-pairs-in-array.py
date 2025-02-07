class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:

        count_pair=0
        prev_occ = set()

        for num in nums:

            if  num in prev_occ:
                prev_occ.remove(num)
                count_pair += 1

                continue

            prev_occ.add(num)
        return [count_pair , len(nums)- (count_pair * 2)]
        