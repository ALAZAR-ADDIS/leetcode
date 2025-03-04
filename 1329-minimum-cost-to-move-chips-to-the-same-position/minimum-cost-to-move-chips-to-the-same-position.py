class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        count = defaultdict(int)

        for i in range(len(position)):
            count[position[i] % 2] += 1
        
        return min(count[0],count[1])
        