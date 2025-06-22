class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans = []
        heapq.heapify(nums)

        for i in range(len(nums)//2):
            a = heapq.heappop(nums)
            b = heapq.heappop(nums)
            ans.append(b)
            ans.append(a)
        return ans
        