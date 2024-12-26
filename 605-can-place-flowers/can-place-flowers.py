class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # flowerdPlots=set()   


        # for r in range(len(flowerbed)):
        #     if flowerbed[r]==0 and r not in flowerdPlots :
        #         if len(flowerbed)>1 and  r==0 and flowerbed[r+1]==0:
        #             flowerdPlots.add(r)
        #             n-=1
        #         elif  r-1 not in flowerdPlots and r==len(flowerbed)-1 and flowerbed[r-1]==0:
        #             flowerdPlots.add(r)
        #             n-=1
        #         elif  r-1 not in flowerdPlots and flowerbed[r-1]==0 and flowerbed[r+1]==0:
        #             flowerdPlots.add(r)
        #             n-=1
        # return  True  if n<=0 else False

        FlowerB=[0]+flowerbed+[0]

        for i in range(1,len(FlowerB)-1):
            if FlowerB[i]==0 and FlowerB[i-1]==0 and FlowerB[i+1]==0:
                n-=1
                FlowerB[i]=1
        return  True  if n<=0 else False
        
        
        