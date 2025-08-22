class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        p = [(-val,i) for i,val in enumerate(nums)]
        heapq.heapify(p)
        ans = []
        for i in range(k):
            val,index = heapq.heappop(p)
            ans.append((-val,index))
        ans.sort(key = lambda x:x[1])
        ans2 = []
        for val, index in ans:
            ans2.append(val)
        return ans2

        