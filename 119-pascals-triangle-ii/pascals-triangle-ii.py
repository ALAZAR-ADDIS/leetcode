class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:

            return [1]

           
        else:            
            pascal = self.getRow(rowIndex - 1)

            prev = pascal[0]
            nums = [1]*(rowIndex + 1)

            for i in range(1,len(pascal)):

                nums[i] = pascal[i] + prev
                prev = pascal[i]
            
            return nums

        