class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pot = [0]*(len(flowerbed) + 2)

        for i in  range(len(flowerbed)):
            pot[i + 1] = flowerbed[i]
        

        for i in range(1,len(pot)-1):
            if pot[i - 1] == pot[i] == pot[i + 1] == 0:
                pot[i] = 1
                n -= 1
        return n <= 0

        
        