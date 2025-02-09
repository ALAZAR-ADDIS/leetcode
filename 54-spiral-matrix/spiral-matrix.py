class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        # count = 0

        # right_limit = len(matrix[0])
        # bottom_limit = len(matrix)-1
        # left_limit= len(matrix[0])-1
        # top_limit= len(matrix)-2

        # i = 0
        # j = 0        
        # l=len(matrix[0]) * len(matrix)

        # while count < l :

        #     right=0
        #     while right < right_limit and count < l:

        #             ans.append(matrix[i][j])
        #             j += 1
        #             count += 1 
        #             right+=1          
        #     j -= 1
        #     i += 1       
          
        #     bottom = 0
        #     while bottom < bottom_limit and count < l:
               
        #             ans.append(matrix[i][j])
        #             i += 1
        #             count += 1
        #             bottom+=1
        #     i -=1
        #     j -= 1
                           
        #     left = 0
        #     while left < left_limit and count < l:
               
        #             ans.append(matrix[i][j])
        #             j -= 1
        #             count += 1
        #             left+=1
           
        #     j += 1            
        #     i -= 1

        #     top =0
        #     while top < top_limit and count < l:
            
        #             ans.append(matrix[i][j])
        #             i -= 1
        #             count += 1
        #             top += 1
        #     i += 1            
        #     j += 1

        #     right_limit -= 2
        #     bottom_limit -= 2
        #     left_limit -= 2
        #     top_limit -= 2
        
        # return ans

        #option 2

        top = 0
        left = 0
        bottom = len(matrix)-1
        right = len(matrix[0])-1

        while left <= right and top <= bottom:

            #forward

            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top += 1

            #downward

            for i in range(top,bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            #Backward
            if top <= bottom:
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
            
            #up
            if left <= right:
                for i in range(bottom, top-1,-1):
                    ans.append(matrix[i][left])
                left += 1
        return ans
        