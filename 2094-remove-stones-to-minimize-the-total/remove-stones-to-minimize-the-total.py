class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        p = [-i for i in piles]
        heapq.heapify(p)
        for i  in  range(k):
            curr = -heapq.heappop(p)
            curr = curr - (curr//2)
            heapq.heappush(p, -curr)
        return -sum(p)



       
      
        

        
        