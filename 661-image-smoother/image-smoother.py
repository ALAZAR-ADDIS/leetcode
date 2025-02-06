class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ans=[]

        for i in range(len(img)):
            curr_list = []
            for j in range(len(img[0])):

                total=0
                count=0

                for row in range(i-1,i+2):
                    for col in range(j-1, j+2):

                        if 0 <= row < len(img) and 0<= col <len(img[0]):
                            total +=  img[row][col]
                            count += 1

                curr_list.append(total//count)
            ans.append(curr_list)
        return ans
            
                    

        