class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Bubble sort algorithm
        # for i in range(len(heights)):
        #     isChanged=False
        #     for j in range(1,len(heights)-i):
                
        #         if heights[j-1]<heights[j]:
        #             heights[j-1],heights[j]= heights[j],heights[j-1]
        #             names[j-1],names[j]= names[j],names[j-1]
        #             isChanged=True
        #     if not isChanged:
        #         return names
        # return names

        # selection sort

        # for i in range(len(heights)):
        #     maxIndex=i
        #     for j in range(i+1,len(heights)):
        #         if heights[maxIndex]<heights[j]:
        #             maxIndex=j
        #     heights[maxIndex],heights[i]=heights[i],heights[maxIndex]
        #     names[maxIndex],names[i]=names[i],names[maxIndex]
        # return names

        #inseertion sort
        
        for i  in range(1,len(heights)):
            j=i-1
            maxNum=heights[i]
            maxName=names[i]
            while j>=0 and heights[j]<maxNum:
                heights[j+1],heights[j]=heights[j],heights[j+1]
                names[j+1],names[j]=names[j],names[j+1]
                j-=1
            heights[j+1]=maxNum
            names[j+1]=maxName
        print(heights)
        return names
                



                    


        
        