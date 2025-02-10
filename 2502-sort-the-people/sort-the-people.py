class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        # for i in range(len(heights)-1):
        #     for j in range(len(heights)-i-1):
        #         if heights[j] < heights[j+1]:
                    # heights[j] , heights[j+1] = heights[j+1], heights[j]
                    # names[j] , names[j+1] = names[j+1], names[j]
       
        # return names
        # for i in range(len(heights)):
        #     max_index= i
        #     for j in range(i+1,len(heights)):
        #         if heights[max_index] < heights[j]:
        #             max_index =j
            
        #     heights[i] , heights[max_index] = heights[max_index],  heights[i]
        #     names[i] , names[max_index] = names[max_index], names[i]
        # return names


        # for i in range(1,len(heights)):
        #     j= i-1
        #     temp_h = heights[i]
        #     temp_n = names[i]
            

        #     while j>=0 and heights[j] < temp_h:

        #         heights[j+1] = heights[j]  
        #         names[j+1] = names[j]
        #         j-=1
        #     names[j+1] = temp_n
        #     heights[j+1] = temp_h
            
            
        # return names
        
        dict_pair = {}
        for i in range(len(names)):
            dict_pair[heights[i]] = names[i]
        
        max_val = max(heights)
        counter = [0]*(max_val + 1)

        for i in  heights:
            counter[i] += 1
        
        ans = []

        for  i in range(len(counter)-1,-1,-1):
            j = counter[i]
            while  j>0:
                ans.append(dict_pair[i])
                j-=1
        return ans
        







        