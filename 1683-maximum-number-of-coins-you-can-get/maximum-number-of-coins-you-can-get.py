class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse= True)
      
    
        l=1
        r =len(piles)-1
        maxx = 0

        while l < r:
            print(piles[l])
            maxx += piles[l]
            l+=2
            r -= 1
        
        return maxx
        