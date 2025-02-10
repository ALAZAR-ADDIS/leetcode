class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        # for i in range(len(heights)-1):
        #     for j in range(len(heights)-i-1):
        #         if heights[j] < heights[j+1]:
                    # heights[j] , heights[j+1] = heights[j+1], heights[j]
                    # names[j] , names[j+1] = names[j+1], names[j]
       
        # return names
        for i in range(len(heights)):
            max_index= i
            for j in range(i+1,len(heights)):
                if heights[max_index] < heights[j]:
                    max_index =j
            
            heights[i] , heights[max_index] = heights[max_index],  heights[i]
            names[i] , names[max_index] = names[max_index], names[i]
        return names
            




        