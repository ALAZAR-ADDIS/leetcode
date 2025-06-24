class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        mapp = defaultdict(int)

        for index,val in enumerate(score):
            mapp[val]  = index
        
        heapq.heapify(score)
        ans = [0] * len(score)
        
        while score:
            val = score[0]
            heapq.heappop(score)
            

            if len(score) == 2:
                ans[mapp[val]] = "Bronze Medal"
            elif len(score) == 1:
                ans[mapp[val]] = "Silver Medal"
            elif len(score) == 0:
                ans[mapp[val]] = "Gold Medal"
            else:
                ans[mapp[val]] = f"{len(score) + 1}"
        return ans


        