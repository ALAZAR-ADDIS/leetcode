class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] = - gifts[i]
        heapq.heapify(gifts)

        for i in range(k):
            val = -heapq.heappop(gifts)
            heapq.heappush(gifts,-int(math.sqrt(val)))
        return -sum(gifts)
        