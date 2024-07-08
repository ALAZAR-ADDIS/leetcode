class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort algorithm
        # create 2D list
        numFreq = [[] for i in range(len(nums) + 1)]
        dictFreq = {}
        result = []

        for num in nums:
            dictFreq[num] = 1 + dictFreq.get(num, 0)

        for num, freq in dictFreq.items():
            numFreq[freq].append(num)

        for i in range(len(numFreq) - 1, 0, -1):
            for num in numFreq[i]:
                result.append(num)
                if len(result) == k:
                    return result
