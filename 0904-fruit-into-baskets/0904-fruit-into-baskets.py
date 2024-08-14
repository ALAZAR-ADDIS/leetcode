class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #creat a dictionary of fruits
         #left pointer of my window
         #max number of windows
         #for loop that will have the right pointer of my window
         #add the type  of fruits in the fruit dictionary
         #if  the size of my dicionary above my k value i will  shift the left pointer of my window
         #count the max of fruits in  my dictinary

         fruitT={}
         l=0
         maxf=-1
         for r in range(len(fruits)):
            fruitT[fruits[r]]=1+fruitT.get(fruits[r],0)
            while len(fruitT)>2:
                 fruitT[fruits[l]]=-1+fruitT[fruits[l]]
                 if fruitT[fruits[l]]==0:
                     fruitT.pop(fruits[l])
                 l+=1
            maxf=max(maxf,sum(fruitT.values()))

         return maxf
