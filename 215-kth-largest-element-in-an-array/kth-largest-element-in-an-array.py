class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        p = [-i for i in nums]
        heapq.heapify(p)
        
        for i in range(k-1):
            print(heapq.heappop(p))
        
        
        return -p[0]

        